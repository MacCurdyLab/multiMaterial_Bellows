# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/Diameter_25mm--WallThick_1-1mm"

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")            # Agilus
blue = materials.id("blue")          # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")        # Support
yellow = materials.id("yellow")      # Air

#-- Dimensions of part --
mainHeight = 3.5   # Dr. Mac's: 3.5[mm]
mainD = 25         # Dr. Mac's: 25[mm]
capHeight = 1      #[mm]

#-- Stack Settings --
fluidPercent = 0.725
numStacks = 3
includeBaffles = False
fluidPercent = 0.725

#-- placing stuff --
x = 0
y = 0
z = 0

#-- Defining Root Node --
root = pv.Union()

#-----------------------------------------------------
#-- Importing meshes ---------------------------------
#-----------------------------------------------------

#-- Outter Bellow --
bellows1 = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - Variable_Bellow-1.STL", red)
bellows1 = pv.Translate(-x-mainD/2, -y-mainD/2,0 , bellows1)

# === MATERIAL GRADING ===
# Gradient Type: gradient3
# Design Type: Single stack
# Stiff Section Settings: 70% Vero, 30% Agilus
# Soft  Section Settings: 20% Vero, 80% Agilus
# Gradient Start / End:   85% → 80%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 85,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.6833333333 -0.0278260529 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.2588367052 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0459893736 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.1194344455 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0226838896 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0203454022 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0021069938 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0166126908 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0131943242 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0110097350 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0054177078 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0014714652 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0061193102 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0040641645 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0063310974 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0007210749 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0013995593 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0008065000 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0048288665 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0011271346 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0000480896 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0026991233 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0009169382 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0018858933 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0003046779 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0009368641 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0011454427 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0015461294 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0009306646 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0000396798 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0007331487 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0008173817 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0012690291 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0002699586 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0000541888 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0002307043 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0011547026 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0000643409 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0005005152 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0000186958 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0007222100 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0002137416 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0007179351 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0001334321 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0002336623 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0003191604 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0006100098 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0003700826 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0000908084 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0001956052 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0003415380 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0005211296 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0001721104 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0000589106 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0001051913 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0004859561 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0000749446 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0002897720 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0000164178 * cos(60*pi ((x^2 + y^2)^0.5)/15) +0.0002961898 * cos(61*pi ((x^2 + y^2)^0.5)/15) +0.0000629853 * cos(62*pi ((x^2 + y^2)^0.5)/15) -0.0003852485 * cos(63*pi ((x^2 + y^2)^0.5)/15) -0.0000744770 * cos(64*pi ((x^2 + y^2)^0.5)/15) -0.0000654938 * cos(65*pi ((x^2 + y^2)^0.5)/15) -0.0001225718 * cos(66*pi ((x^2 + y^2)^0.5)/15) +0.0003285894 * cos(67*pi ((x^2 + y^2)^0.5)/15) +0.0001933123 * cos(68*pi ((x^2 + y^2)^0.5)/15) -0.0000924090 * cos(69*pi ((x^2 + y^2)^0.5)/15) +0.0000638255 * cos(70*pi ((x^2 + y^2)^0.5)/15) -0.0001871196 * cos(71*pi ((x^2 + y^2)^0.5)/15) -0.0002703439 * cos(72*pi ((x^2 + y^2)^0.5)/15) +0.0001271177 * cos(73*pi ((x^2 + y^2)^0.5)/15) +0.0000699846 * cos(74*pi ((x^2 + y^2)^0.5)/15) +0.0000577715 * cos(75*pi ((x^2 + y^2)^0.5)/15) +0.0002486654 * cos(76*pi ((x^2 + y^2)^0.5)/15) -0.0000663116 * cos(77*pi ((x^2 + y^2)^0.5)/15) -0.0001951826 * cos(78*pi ((x^2 + y^2)^0.5)/15) -0.0000072820 * cos(79*pi ((x^2 + y^2)^0.5)/15) -0.0001406716 * cos(80*pi ((x^2 + y^2)^0.5)/15) -0.0000161129 * cos(81*pi ((x^2 + y^2)^0.5)/15) +0.0002446632 * cos(82*pi ((x^2 + y^2)^0.5)/15) +0.0000408563 * cos(83*pi ((x^2 + y^2)^0.5)/15) +0.0000079634 * cos(84*pi ((x^2 + y^2)^0.5)/15) +0.0000516341 * cos(85*pi ((x^2 + y^2)^0.5)/15)",
          "0.3166666667 +0.0278260529 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.2588367052 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0459893736 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.1194344455 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0226838896 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0203454022 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0021069938 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0166126908 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0131943242 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0110097350 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0054177078 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0014714652 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0061193102 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0040641645 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0063310974 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0007210749 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0013995593 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0008065000 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0048288665 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0011271346 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0000480896 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0026991233 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0009169382 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0018858933 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0003046779 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0009368641 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0011454427 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0015461294 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0009306646 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0000396798 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0007331487 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0008173817 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0012690291 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0002699586 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0000541888 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0002307043 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0011547026 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0000643409 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0005005152 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0000186958 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0007222100 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0002137416 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0007179351 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0001334321 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0002336623 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0003191604 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0006100098 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0003700826 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0000908084 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0001956052 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0003415380 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0005211296 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0001721104 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0000589106 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0001051913 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0004859561 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0000749446 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0002897720 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0000164178 * cos(60*pi ((x^2 + y^2)^0.5)/15) -0.0002961898 * cos(61*pi ((x^2 + y^2)^0.5)/15) -0.0000629853 * cos(62*pi ((x^2 + y^2)^0.5)/15) +0.0003852485 * cos(63*pi ((x^2 + y^2)^0.5)/15) +0.0000744770 * cos(64*pi ((x^2 + y^2)^0.5)/15) +0.0000654938 * cos(65*pi ((x^2 + y^2)^0.5)/15) +0.0001225718 * cos(66*pi ((x^2 + y^2)^0.5)/15) -0.0003285894 * cos(67*pi ((x^2 + y^2)^0.5)/15) -0.0001933123 * cos(68*pi ((x^2 + y^2)^0.5)/15) +0.0000924090 * cos(69*pi ((x^2 + y^2)^0.5)/15) -0.0000638255 * cos(70*pi ((x^2 + y^2)^0.5)/15) +0.0001871196 * cos(71*pi ((x^2 + y^2)^0.5)/15) +0.0002703439 * cos(72*pi ((x^2 + y^2)^0.5)/15) -0.0001271177 * cos(73*pi ((x^2 + y^2)^0.5)/15) -0.0000699846 * cos(74*pi ((x^2 + y^2)^0.5)/15) -0.0000577715 * cos(75*pi ((x^2 + y^2)^0.5)/15) -0.0002486654 * cos(76*pi ((x^2 + y^2)^0.5)/15) +0.0000663116 * cos(77*pi ((x^2 + y^2)^0.5)/15) +0.0001951826 * cos(78*pi ((x^2 + y^2)^0.5)/15) +0.0000072820 * cos(79*pi ((x^2 + y^2)^0.5)/15) +0.0001406716 * cos(80*pi ((x^2 + y^2)^0.5)/15) +0.0000161129 * cos(81*pi ((x^2 + y^2)^0.5)/15) -0.0002446632 * cos(82*pi ((x^2 + y^2)^0.5)/15) -0.0000408563 * cos(83*pi ((x^2 + y^2)^0.5)/15) -0.0000079634 * cos(84*pi ((x^2 + y^2)^0.5)/15) -0.0000516341 * cos(85*pi ((x^2 + y^2)^0.5)/15)"
    ],
    [red, blue],
    True
)
bellows_fgrade.set_child(bellows1)

# Translate into position:
bellows_fgrade = pv.Translate(x+mainD/2, y+mainD/2, 0, bellows_fgrade)


# -- Caps --
cap1_mesh = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - CloseCap-1.STL",red)
cap1fgrade = pv.FGrade(["0.95", "0.05"], [blue, red], True )
cap1fgrade.set_child(cap1_mesh)

cap2_mesh = pv.Mesh(
    STL_Location+"/variableNumberBellowsStack_ASSEMBLY - domeCap-1.STL",red)
cap2fgrade =  pv.FGrade(["0.95", "0.05"], [blue, red], True )
cap2fgrade.set_child(cap2_mesh)
cap2_mesh = cap2fgrade

cap2_mesh = pv.Translate(0,0,numStacks*mainHeight+capHeight,cap2_mesh)

# -- Fluid-Solid Support Barrier --
supportBarrier1_mesh = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - Variable_SupportBundary-1.STL",green
)

# -- Baffles and Fluid --
fluidNoHoles1_mesh = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - Variable_Fluid-2.STL", liquid_mat
)
fluidAir_fgrade = pv.FGrade([str(fluidPercent),str(1-fluidPercent)],[liquid_mat,yellow],True)

if includeBaffles == True:
    fluidHoles1_mesh = pv.Mesh(
        STL_Location + "/variableNumberBellowsStack_ASSEMBLY - Variable_Fluid-1.STL", liquid_mat
    )
    baffles = pv.Difference(fluidNoHoles1_mesh, fluidHoles1_mesh)
    bafflesFgrade = pv.FGrade(['1'], [green], True)
    bafflesFgrade.set_child(baffles)
    fluidAir_fgrade.set_child(fluidHoles1_mesh)
else:
    fluidAir_fgrade.set_child(fluidNoHoles1_mesh)


#--------------------------------------------------------
#-- Repeating each Bellows Assmbly for N Bellows Stack --
#--------------------------------------------------------
repeatUnion = pv.Union()
repeatUnion.add_child(bellows_fgrade)
repeatUnion.add_child(supportBarrier1_mesh)
repeatUnion.add_child(fluidAir_fgrade)

if includeBaffles == True:
    repeatUnion.add_child(bafflesFgrade)

# Union node for the entire stack of baffles excluding caps
fullStackUnion = pv.Union()
fullStackUnion.add_child(repeatUnion)

for i in range(numStacks-1):
    tempBellowsMesh = repeatUnion
    tempBellowsMesh = pv.Translate(0,0,mainHeight*(i+1),tempBellowsMesh)
    fullStackUnion.add_child(tempBellowsMesh)

#--------------------------------------
#-- Union of all Meshes to Root Node --
#--------------------------------------
root.add_child(fullStackUnion)
root.add_child(cap1fgrade)
root.add_child(cap2_mesh)

#-- Section View --
#tempRect = pv.RectPrism(pv.Vec3(x+mainD/2,y+mainD/2,0),pv.Vec3(mainD,mainD,4),red)
#root = pv.Difference(root,tempRect)