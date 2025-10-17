# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/Sloped_Cap_wALLtHICKNESS0-8"

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
BottomcapHeight = 2      #[mm]
topCapHeight = 1.2 #[mm]

#-- Stack Settings --
fluidPercent = 0.725
numStacks = 3
includeBaffles = True
num_bellowsToPrint = 1

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
# Soft  Section Settings: 15% Vero, 85% Agilus
# Gradient Start / End:   87.5% → 85%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 60,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.7083333333 -0.0264378881 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.2674991665 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0488263360 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.1330534765 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0283434787 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0253984125 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0021223405 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0181241036 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0158514018 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0131507473 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0063659397 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0013423558 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0071936645 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0047199318 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0074066595 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0009484926 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0015623292 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0008355726 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0056440195 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0000108156 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0013959531 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0001469943 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0031384654 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0010846684 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0022476002 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0003107282 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0010622381 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0013544519 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0018121422 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0010807623 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0000842552 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0008657901 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0009360122 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0014930505 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0003443256 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0000634476 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0002430390 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0013568280 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0000868943 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0005908818 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0008400409 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0002536608 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0008455865 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0001442093 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0002598078 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0003840765 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0007148577 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0004295275 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0001211060 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0002378337 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0003942296 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0006104970 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0002109176 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0000661677 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0001128214 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0005692992 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0000895314 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0003415138 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0000082089 * cos(60*pi ((x^2 + y^2)^0.5)/15)",
          "0.2916666667 +0.0264378881 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.2674991665 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0488263360 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.1330534765 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0283434787 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0253984125 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0021223405 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0181241036 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0158514018 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0131507473 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0063659397 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0013423558 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0071936645 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0047199318 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0074066595 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0009484926 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0015623292 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0008355726 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0056440195 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0000108156 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0013959531 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0001469943 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0031384654 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0010846684 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0022476002 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0003107282 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0010622381 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0013544519 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0018121422 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0010807623 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0000842552 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0008657901 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0009360122 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0014930505 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0003443256 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0000634476 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0002430390 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0013568280 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0000868943 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0005908818 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0008400409 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0002536608 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0008455865 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0001442093 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0002598078 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0003840765 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0007148577 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0004295275 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0001211060 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0002378337 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0003942296 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0006104970 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0002109176 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0000661677 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0001128214 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0005692992 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0000895314 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0003415138 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0000082089 * cos(60*pi ((x^2 + y^2)^0.5)/15)"
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
    STL_Location+"/slopedStart_domeCap_v2.STL",red)
cap2_mesh = pv.Translate(-20.186845/2-.1562775,-5.2/2,-20.5/2,cap2_mesh)
cap2_mesh = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),cap2_mesh)
cap2_mesh = pv.Translate(x+mainD/2,y+mainD/2,2.600002,cap2_mesh)
cap2fgrade =  pv.FGrade(["0.95", "0.05"], [blue, red], True )
cap2fgrade.set_child(cap2_mesh)
cap2_mesh = cap2fgrade

cap2_mesh = pv.Translate(0,0,numStacks*mainHeight+topCapHeight,cap2_mesh)

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

# -- Support Cap --
supportCap_H = 0.6; #[mm]
supportCap = pv.Cylinder(pv.Vec3(x+mainD/2,y+mainD/2,2+numStacks*mainHeight+supportCap_H/2-0.3),3.5/2,supportCap_H,green)


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

fullStackUnion = pv.Difference(fullStackUnion,supportCap)

#--------------------------------------
#-- Union of all Meshes to Root Node --
#--------------------------------------
# Using a temporaty union before adding to root incase of multiprint
singleStack_Union = pv.Union()
singleStack_Union.add_child(fullStackUnion)
singleStack_Union.add_child(cap1fgrade)
singleStack_Union.add_child(cap2_mesh)
singleStack_Union.add_child(supportCap)

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
tempRect = pv.RectPrism(pv.Vec3(x,y,(numStacks*mainHeight)/2+topCapHeight),pv.Vec3(50,25,40),red)
root = pv.Difference(root,tempRect)