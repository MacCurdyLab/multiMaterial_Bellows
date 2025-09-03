#include <Arduino.h>
#include <math.h>         // for fabs()
#include <SPI.h>
#include <RTClib.h>

// --- Encoder & Motor Driver Pins ---
const int ENCA_PIN            = 2;    // Encoder channel A (interrupt)
const int ENCB_PIN            = 3;    // Encoder channel B
const int RPWM_PIN            = 9;    // BTS7960 forward PWM
const int LPWM_PIN            = 10;   // BTS7960 reverse PWM
const int R_EN_PIN            = 25;   // BTS7960 forward enable
const int L_EN_PIN            = 23;   // BTS7960 reverse enable

// --- Encoder & PID parameters ---
float PWM_CONSTANT = 200;

// --- RTC Parameters ---
#define RTC_SDA       20
#define RTC_SCL       21

// --- Sensor Parameters ---
const uint8_t sensorPins[4] = { A0, A1, A2, A3 };
long resistanceValue = 0;


void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  // Motor driver setup
  pinMode(RPWM_PIN, OUTPUT);
  pinMode(LPWM_PIN, OUTPUT);
  pinMode(R_EN_PIN, OUTPUT);
  pinMode(L_EN_PIN, OUTPUT);
  digitalWrite(R_EN_PIN, HIGH);
  digitalWrite(L_EN_PIN, HIGH);

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

  // Turn on Motor
  analogWrite(RPWM_PIN, PWM_CONSTANT);
  analogWrite(LPWM_PIN, 0);
}

void loop() {
  // Printing Resistance values to serial plotter
  Serial.print("Sensor_1:");
  Serial.print(analogRead(sensorPins[0]));
  Serial.print(",")
  Serial.print("Sensor_2:");
  Serial.print(analogRead(sensorPins[1]));
  Serial.print(",")
  Serial.print("Sensor_3:");
  Serial.print(analogRead(sensorPins[2]));
  Serial.print(",")
  Serial.print("Sensor_4:");
  Serial.println(analogRead(sensorPins[3]));
  
}
