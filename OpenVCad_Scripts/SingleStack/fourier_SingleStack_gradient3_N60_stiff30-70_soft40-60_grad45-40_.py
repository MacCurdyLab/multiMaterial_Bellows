# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/EdgeTHickness_2-25.WallThickness_0-8"

#-- Material definitions --
materials = pv.default_materials()
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
fluidPercent = 1
numStacks = 3
includeBaffles = True
num_bellowsToPrint = 4

#-- placing stuff --
x = 3.862658
y = 3.861415
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
# Soft  Section Settings: 60% Vero, 40% Agilus
# Gradient Start / End:   45% → 40%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 60,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.3944444444 -0.0111262374 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.0747289533 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0115471747 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.0216527738 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0000151778 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0000444537 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0006818690 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0035223466 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0008553380 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0008152287 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0005415934 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0006626342 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0006072977 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0004803651 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0006762830 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0000628653 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0002494933 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0002300699 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0005227515 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0000172868 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0001158431 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0003139183 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0000820057 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0001463552 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0000934923 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0001451227 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0001031352 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0001606926 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0001100912 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0000462073 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0000675276 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0001142867 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0001243146 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0000091698 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0000057179 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0000604551 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0001154004 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0000086243 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0000463497 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0000308608 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0000836288 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0000180216 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0000691099 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0000301077 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0000430268 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0000198321 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0000635394 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0000441011 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0000101275 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0000088971 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0000435906 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0000545533 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0000056272 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0000099607 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0000248903 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0000508612 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0000055325 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0000276015 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0000164178 * cos(60*pi ((x^2 + y^2)^0.5)/15)",
          "0.6055555556 +0.0111262374 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.0747289533 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0115471747 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.0216527738 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0000151778 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0000444537 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0006818690 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0035223466 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0008553380 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0008152287 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0005415934 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0006626342 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0006072977 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0004803651 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0006762830 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0000628653 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0002494933 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0002300699 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0005227515 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0000172868 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0001158431 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0003139183 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0000820057 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0001463552 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0000934923 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0001451227 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0001031352 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0001606926 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0001100912 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0000462073 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0000675276 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0001142867 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0001243146 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0000091698 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0000057179 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0000604551 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0001154004 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0000086243 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0000463497 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0000308608 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0000836288 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0000180216 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0000691099 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0000301077 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0000430268 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0000198321 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0000635394 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0000441011 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0000101275 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0000088971 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0000435906 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0000545533 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0000056272 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0000099607 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0000248903 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0000508612 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0000055325 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0000276015 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0000164178 * cos(60*pi ((x^2 + y^2)^0.5)/15)"
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
# Using a temporaty union before adding to root incase of multiprint
singleStack_Union = pv.Union()
singleStack_Union.add_child(fullStackUnion)
singleStack_Union.add_child(cap1fgrade)
singleStack_Union.add_child(cap2_mesh)

root.add_child(singleStack_Union)

#---------------------------
#-- Translation for MultiPrint
#--------------------------------

#We want to do multiprint if num_bellowsToPrint > 1
if num_bellowsToPrint > 1:
    tempStack  = singleStack_Union
    for i in range(num_bellowsToPrint-1):
        tempStack = pv.Translate(60,8,0,tempStack)
        root.add_child(tempStack)

#-- Section View --
#Bottom
#tempRect = pv.RectPrism(pv.Vec3(x+mainD/2,y+mainD/2,0),pv.Vec3(mainD,mainD,8),red)
#Side
#tempRect = pv.RectPrism(pv.Vec3(x,y,(numStacks*mainHeight)/2+topCapHeight),pv.Vec3(50,25,20),red)
#root = pv.Difference(root,tempRect)