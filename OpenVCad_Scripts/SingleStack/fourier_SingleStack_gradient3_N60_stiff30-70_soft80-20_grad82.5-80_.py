# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "../STL Files/VariableSingleStack/Diameter_25mm--WallThick_1-1mm"

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
includeBaffles = True
fluidPercent = 0.725

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
# Soft  Section Settings: 20% Vero, 80% Agilus
# Gradient Start / End:   82.5% → 80%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 60,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.6722222222 -0.0243504112 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.2444856975 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0445210612 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.1208307676 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0255098897 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0228607939 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0019441999 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0164878106 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0143090285 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0118764340 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0057564254 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0012412520 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0065046629 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0042719569 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0066998077 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0008505001 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0014185709 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0007635188 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0051057551 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0000108156 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0012572221 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0001265027 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0028403148 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0009803019 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0020301579 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0002843300 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0009632704 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0012241635 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0016389626 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0009781906 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0000735194 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0007825875 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0008481253 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0013499611 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0003094346 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0000573888 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0002217579 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0012269152 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0000777737 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0005341111 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0000017448 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0007602182 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0002291958 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0007644833 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0001312938 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0002359783 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0003466604 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0006465489 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0003887798 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0001084891 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0002144952 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0003569862 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0005521750 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0001901072 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0000600490 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0001027838 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0005149124 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0000808549 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0003087425 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0000082089 * cos(60*pi ((x^2 + y^2)^0.5)/15)",
          "0.3277777778 +0.0243504112 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.2444856975 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0445210612 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.1208307676 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0255098897 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0228607939 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0019441999 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0164878106 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0143090285 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0118764340 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0057564254 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0012412520 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0065046629 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0042719569 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0066998077 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0008505001 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0014185709 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0007635188 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0051057551 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0000108156 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0012572221 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0001265027 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0028403148 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0009803019 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0020301579 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0002843300 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0009632704 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0012241635 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0016389626 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0009781906 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0000735194 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0007825875 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0008481253 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0013499611 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0003094346 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0000573888 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0002217579 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0012269152 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0000777737 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0005341111 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0000017448 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0007602182 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0002291958 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0007644833 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0001312938 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0002359783 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0003466604 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0006465489 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0003887798 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0001084891 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0002144952 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0003569862 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0005521750 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0001901072 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0000600490 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0001027838 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0005149124 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0000808549 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0003087425 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0000082089 * cos(60*pi ((x^2 + y^2)^0.5)/15)"
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