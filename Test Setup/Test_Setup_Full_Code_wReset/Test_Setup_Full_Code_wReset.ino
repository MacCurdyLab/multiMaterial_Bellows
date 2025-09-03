#include <Arduino.h>
#include <math.h>         // for fabs()
#include <SPI.h>
#include <SD.h>
#include <RTClib.h>
#include <LiquidCrystal.h>

// --- Encoder & Motor Driver Pins ---
const int ENCA_PIN            = 2;    // Encoder channel A (interrupt)
const int ENCB_PIN            = 3;    // Encoder channel B
const int RPWM_PIN            = 9;    // BTS7960 forward PWM
const int LPWM_PIN            = 10;   // BTS7960 reverse PWM
const int R_EN_PIN            = 25;   // BTS7960 forward enable
const int L_EN_PIN            = 23;   // BTS7960 reverse enable

// --- Encoder & PID parameters ---
volatile long encoderCount    = 0;
const float PULSES_PER_REV    = 751.8;            // your encoder spec
const unsigned long CONTROL_INTERVAL_MS = 200;    // 100 ms loop
static unsigned long lastControlTime = 0;
float PWM_CONSTANT = 200;


float setPointRPM = 25.0; //default is 50.0
float Kp = 0.6, Ki = 0.02, Kd = 0.001; // Default is 0.5, 0.02, 0.001
const float I_MAX   = 20000.0;
const int   PWM_MAX = 250;
const int   MAX_STEP= 10;
float rpm = 0.0;

float integral = 0.0, prevError = 0.0;
int   lastPwm  = 0.8;

// ISR: on A rising, read B to determine direction
void onEncoderA() {
  encoderCount += (digitalRead(ENCB_PIN) == HIGH) ? +1 : -1;
}

// --- SD / RTC / LCD / Sensors from your original sketch ---
#define SD_CS         53   // SD card CS pin on Mega
#define RTC_SDA       20
#define RTC_SCL       21
const unsigned long RECORD_INTERRVAL_MS = 3000;
unsigned long LAST_RECORD_TIME_MS = 0;

// --- LCD SETUP ---
LiquidCrystal lcd(7, 6, 5, 4, 11, 29); 
RTC_DS3231 rtc;
File logFile;

const uint8_t resetButtonPin = 8;
uint16_t fileIndex = 1;
char currentFilename[20];

const uint8_t sensorPins[4] = { A0, A1, A2, A3 };
const int threshold = 725; // originally 512
uint8_t prevState[4] = { 0, 0, 0, 0 };
uint32_t pressCount[4] = { 0, 0, 0, 0 };

bool latchInitCaptured = false;
uint8_t latchStateAtMotorOff = HIGH;
uint32_t lastPressEpoch = 0;

void updateFilename() {
  snprintf(currentFilename, sizeof(currentFilename), "LOG%04u.TXT", fileIndex);
}
void createNewLogFile() {
  updateFilename();
  logFile = SD.open(currentFilename, FILE_WRITE);
  if (logFile) {
    logFile.println(F("Timestamp,Sensor_1,Sensor_2,Senosr_3,Sensor_4"));
    logFile.close();
  } else {
    Serial.print(F("createNewLogFile failed for "));
    Serial.println(currentFilename);
  }
}
void resetCountersAndStates() {
  for (uint8_t i = 0; i < 4; i++) {
    pressCount[i] = 0;
    int v = analogRead(sensorPins[i]);
    prevState[i] = (v > threshold) ? 1 : 0;
  }
}
void printFilenameToLCD() {
  lcd.setCursor(0, 3);
  lcd.print(currentFilename);
  int len = strlen(currentFilename);
  while (len++ < 20) lcd.print(' ');
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  // LCD
  lcd.begin(20, 4);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(F("Initializing..."));
  delay(500);
  lcd.clear();
  printFilenameToLCD();

  // Motor driver setup
  pinMode(RPWM_PIN, OUTPUT);
  pinMode(LPWM_PIN, OUTPUT);
  pinMode(R_EN_PIN, OUTPUT);
  pinMode(L_EN_PIN, OUTPUT);
  digitalWrite(R_EN_PIN, HIGH);
  digitalWrite(L_EN_PIN, HIGH);

  // Encoder setup
  pinMode(ENCA_PIN, INPUT_PULLUP);
  pinMode(ENCB_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENCA_PIN), onEncoderA, RISING);

  // Button
  pinMode(resetButtonPin, INPUT_PULLUP);

  // RTC
  if (!rtc.begin()) {
    Serial.println(F("RTC not found"));
    lcd.setCursor(0, 0);
    lcd.print("RTC not Found");
    lcd.setCursor(1,0);
    lcd.print("Please Connect Clock and Restart");
    while (1);
  }
  //rtc.adjust(DateTime(F(__DATE__), F(__TIME__))); // run once, then comment

  // SD
  if (!SD.begin(SD_CS)) {
    Serial.println(F("SD init failed"));
    lcd.setCursor(0, 0);
    lcd.print("SD Card not Found");
    lcd.setCursor(1,0);
    lcd.print("Please Insert SD Card and Restart");

    while (1);
  }

  createNewLogFile();
  resetCountersAndStates();

  DateTime now = rtc.now();
  lastPressEpoch = now.unixtime();

  
}

void loop() {
  DateTime now = rtc.now();
  uint32_t currentEpoch = now.unixtime();

  // 1) Decide whether the motor should run
  bool motorShouldRun = (currentEpoch - lastPressEpoch) <= 5;

  // 2) Encoder-PID  control, every CONTROL_INTERVAL_MS when running
  // static unsigned long lastControlTime = 0;
  unsigned long m = millis();
  if (motorShouldRun) {
    if (m - lastControlTime >= CONTROL_INTERVAL_MS) {
      lastControlTime += CONTROL_INTERVAL_MS;
      // grab & reset count
      noInterrupts();
      long c = encoderCount;
      encoderCount = 0;
      interrupts();
      // compute RPM
      float revs   = c / PULSES_PER_REV;
      float rpmRaw = revs * (60000.0 / CONTROL_INTERVAL_MS);
      float rpm    = fabs(rpmRaw);
      // PID
      float error  = setPointRPM - rpm;
      float Pout   = Kp * error;
      integral    += error * CONTROL_INTERVAL_MS;
      integral     = constrain(integral, -I_MAX, I_MAX);
      float Iout   = Ki * integral;
      float derivative = (error - prevError) / CONTROL_INTERVAL_MS;
      float Dout   = Kd * derivative;
      prevError    = error;
      float out    = Pout + Iout + Dout;
      int pwm      = constrain(int(abs(out)), 0, PWM_MAX);
      int delta    = pwm - lastPwm;
      if      (delta >  MAX_STEP) pwm = lastPwm + MAX_STEP;
      else if (delta < -MAX_STEP) pwm = lastPwm - MAX_STEP;
      lastPwm = pwm;
      // drive
      // If you want PID controls switch PWM_CONSTANT to pwm in the following loop
      if (out >= 0) {
        analogWrite(RPWM_PIN, PWM_CONSTANT);
        analogWrite(LPWM_PIN, 0);
      } else {
        analogWrite(RPWM_PIN, PWM_CONSTANT);
        analogWrite(LPWM_PIN, 0);
      }
      // debug
      Serial.print("RPM: "); Serial.print(rpm);
      //Serial.print(",");
      Serial.print("  Err: "); Serial.print(error);
      //Serial.print(",");
      Serial.print("  PWM: "); Serial.println(pwm);
      //Serial.print(",");

      lcd.setCursor(0,0);
      lcd.print("RPM: "); lcd.print((int)rpm);
  

    }
  } else {
    // ensure motor is stopped
    analogWrite(RPWM_PIN, 0);
    analogWrite(LPWM_PIN, 0);
  }

  // 3) When motor’s off, handle latch-reset to start new file
  if (!motorShouldRun) {
    if (!latchInitCaptured) {
      latchStateAtMotorOff = digitalRead(resetButtonPin);
      latchInitCaptured = true;
    } else {
      uint8_t curr = digitalRead(resetButtonPin);
      if (curr != latchStateAtMotorOff) {
        fileIndex++;
        createNewLogFile();
        resetCountersAndStates();
        Serial.print(F("Switched to new log: "));
        Serial.println(currentFilename);
        lastPressEpoch = currentEpoch;  // run again
        printFilenameToLCD();
        latchInitCaptured = false;
      }
    }
  } else {
    latchInitCaptured = false;
  }

  // 4) Sensor reading & SD logging on each rising edge
  for (uint8_t i = 0; i < 4; i++) {
    int v = analogRead(sensorPins[i]);
    // Serial.print("Sensor "); Serial.print(i); Serial.print(": "); Serial.println(v);
    uint8_t currState = (v > threshold) ? 1 : 0;
    if (currState && !prevState[i]) {
      pressCount[i]++;
      lastPressEpoch = currentEpoch;
      
    }
    prevState[i] = currState;
  }

  if (RECORD_INTERRVAL_MS < m - LAST_RECORD_TIME_MS){
    logFile = SD.open(currentFilename, FILE_WRITE);
    if (logFile) {
    LAST_RECORD_TIME_MS = m;
    int rpmInt = rpm;

    //printing day
    logFile.print(String(now.year())); logFile.print("-"); logFile.print(String(now.month())); logFile.print("-"); logFile.print(String(now.day())); logFile.print(" ");
    //printing time
    logFile.print(String(now.hour())); logFile.print(":"); logFile.print(String(now.minute())); logFile.print(":"); logFile.print(String(now.second()));logFile.print(",");
    //printing press counts
    logFile.print(String(pressCount[0])); logFile.print(","); logFile.print(String(pressCount[1])); logFile.print(","); logFile.print(String(pressCount[2])); logFile.print(",");
    logFile.println(String(pressCount[3]));
    
    logFile.close();
    } else {
      Serial.println(F("Failed to open log file"));
    }

  }
  
  // 5) Update LCD display
  //lcd.setCursor(0, 0);
  //lcd.print("Time:");
  //if (now.hour()   < 10) lcd.print('0');
  ///lcd.print(now.hour()); lcd.print(':');
  //if (now.minute() < 10) lcd.print('0');
  //lcd.print(now.minute()); lcd.print(':');
  //if (now.second() < 10) lcd.print('0');
  //lcd.print(now.second());

  lcd.setCursor(0, 1);
  lcd.print("S1:"); lcd.print(pressCount[0]);
  lcd.print("  S2:"); lcd.print(pressCount[1]);

  lcd.setCursor(0, 2);
  lcd.print("S3:"); lcd.print(pressCount[2]);
  lcd.print("  S4:"); lcd.print(pressCount[3]);

   
  printFilenameToLCD();
  delay(50);
}
