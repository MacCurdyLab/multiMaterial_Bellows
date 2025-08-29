# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack"

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  # Agilus
blue = materials.id("blue")  # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
# Structural material is 95% vero and 5% agilus
# Support Material for support inside liquid and bellows
green = materials.id("green")

#-- Dimensions of part --
mainHeight = 5.0   # Dr. Mac's: 3.5[mm]
mainD = 40.0    # Dr. Mac's: 25[mm]
capHeight = 2.0 #[mm]

#-- Stack Settings --
numStacks = 3
includeBaffles = True

#-- placing stuff --
x = 5.265812
y = 5.263749
z = 0

#-- Defining Root Node --
root = pv.Union()

#----------------------
#-- Importing meshes --
#----------------------

#outter bellow
bellows1 = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - bellow-1.STL", red)
bellows1 = pv.Translate(-x-mainD/2, -y-mainD/2,0 , bellows1)

# === MATERIAL GRADING ===
# Gradient Type: gradient4
# Design Type: Single stack
# Stiff Section Settings: 70% Vero, 30% Agilus
# Soft  Section Settings: 50% Vero, 50% Agilus
# Gradient Start / End:   50% → 50%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 80,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.4514049587 -0.0046208611 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.0847156888 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0106156570 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.0540321307 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0095638543 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0206634787 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0033201079 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0014259788 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0026297887 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0078449984 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0040834197 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0039849814 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0013440557 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0013582986 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0019043751 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0028876978 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0024874145 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0009940967 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0004693039 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0010728088 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0016002139 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0012325464 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0016370954 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0000547391 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0000165526 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0007505863 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0013671077 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0004453847 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0010685718 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0002737617 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0003038455 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0004533847 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0011462092 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0000185788 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0006499272 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0003541144 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0004657494 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0001980945 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0009270313 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0002146559 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0003318489 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0003173217 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0005387958 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0000095979 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0007118725 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0003268025 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0000923993 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0002239137 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0005458294 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0001679189 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0005070069 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0003571094 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0000801967 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0001074304 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0005040047 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0002774384 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0003195632 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0003311233 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0001940898 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0000111649 * cos(60*pi ((x^2 + y^2)^0.5)/15) -0.0004278185 * cos(61*pi ((x^2 + y^2)^0.5)/15) -0.0003407315 * cos(62*pi ((x^2 + y^2)^0.5)/15) +0.0001560670 * cos(63*pi ((x^2 + y^2)^0.5)/15) +0.0002679190 * cos(64*pi ((x^2 + y^2)^0.5)/15) +0.0002565540 * cos(65*pi ((x^2 + y^2)^0.5)/15) +0.0001180307 * cos(66*pi ((x^2 + y^2)^0.5)/15) -0.0003302051 * cos(67*pi ((x^2 + y^2)^0.5)/15) -0.0003622195 * cos(68*pi ((x^2 + y^2)^0.5)/15) +0.0000216324 * cos(69*pi ((x^2 + y^2)^0.5)/15) +0.0001829432 * cos(70*pi ((x^2 + y^2)^0.5)/15) +0.0002751254 * cos(71*pi ((x^2 + y^2)^0.5)/15) +0.0002041673 * cos(72*pi ((x^2 + y^2)^0.5)/15) -0.0002227940 * cos(73*pi ((x^2 + y^2)^0.5)/15) -0.0003479327 * cos(74*pi ((x^2 + y^2)^0.5)/15) -0.0000804972 * cos(75*pi ((x^2 + y^2)^0.5)/15) +0.0000890945 * cos(76*pi ((x^2 + y^2)^0.5)/15) +0.0002579549 * cos(77*pi ((x^2 + y^2)^0.5)/15) +0.0002643438 * cos(78*pi ((x^2 + y^2)^0.5)/15) -0.0001158045 * cos(79*pi ((x^2 + y^2)^0.5)/15) -0.0003051555 * cos(80*pi ((x^2 + y^2)^0.5)/15)",
          "0.5485950413 +0.0046208611 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.0847156888 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0106156570 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.0540321307 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0095638543 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0206634787 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0033201079 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0014259788 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0026297887 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0078449984 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0040834197 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0039849814 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0013440557 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0013582986 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0019043751 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0028876978 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0024874145 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0009940967 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0004693039 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0010728088 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0016002139 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0012325464 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0016370954 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0000547391 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0000165526 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0007505863 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0013671077 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0004453847 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0010685718 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0002737617 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0003038455 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0004533847 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0011462092 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0000185788 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0006499272 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0003541144 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0004657494 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0001980945 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0009270313 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0002146559 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0003318489 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0003173217 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0005387958 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0000095979 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0007118725 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0003268025 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0000923993 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0002239137 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0005458294 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0001679189 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0005070069 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0003571094 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0000801967 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0001074304 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0005040047 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0002774384 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0003195632 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0003311233 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0001940898 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0000111649 * cos(60*pi ((x^2 + y^2)^0.5)/15) +0.0004278185 * cos(61*pi ((x^2 + y^2)^0.5)/15) +0.0003407315 * cos(62*pi ((x^2 + y^2)^0.5)/15) -0.0001560670 * cos(63*pi ((x^2 + y^2)^0.5)/15) -0.0002679190 * cos(64*pi ((x^2 + y^2)^0.5)/15) -0.0002565540 * cos(65*pi ((x^2 + y^2)^0.5)/15) -0.0001180307 * cos(66*pi ((x^2 + y^2)^0.5)/15) +0.0003302051 * cos(67*pi ((x^2 + y^2)^0.5)/15) +0.0003622195 * cos(68*pi ((x^2 + y^2)^0.5)/15) -0.0000216324 * cos(69*pi ((x^2 + y^2)^0.5)/15) -0.0001829432 * cos(70*pi ((x^2 + y^2)^0.5)/15) -0.0002751254 * cos(71*pi ((x^2 + y^2)^0.5)/15) -0.0002041673 * cos(72*pi ((x^2 + y^2)^0.5)/15) +0.0002227940 * cos(73*pi ((x^2 + y^2)^0.5)/15) +0.0003479327 * cos(74*pi ((x^2 + y^2)^0.5)/15) +0.0000804972 * cos(75*pi ((x^2 + y^2)^0.5)/15) -0.0000890945 * cos(76*pi ((x^2 + y^2)^0.5)/15) -0.0002579549 * cos(77*pi ((x^2 + y^2)^0.5)/15) -0.0002643438 * cos(78*pi ((x^2 + y^2)^0.5)/15) +0.0001158045 * cos(79*pi ((x^2 + y^2)^0.5)/15) +0.0003051555 * cos(80*pi ((x^2 + y^2)^0.5)/15)"
    ],
    [red, blue],
    True
)
bellows_fgrade.set_child(bellows1)

# Translate into position:
bellows_fgrade = pv.Translate(x+mainD/2, y+mainD/2, 0, bellows_fgrade)


# Caps
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

# Fluid-Solid support barrier
supportBarrier1_mesh = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - bellow_liquid_supportBarrier-1.STL",green
)

# Baffles and Fluid
fluidNoHoles1_mesh = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - bellow_liquid-1.STL",liquid_mat
)

if includeBaffles == True:
    fluidHoles1_mesh = pv.Mesh(
        STL_Location + "/variableNumberBellowsStack_ASSEMBLY - bellow_liquid-2.STL",liquid_mat
    )
    baffles = pv.Difference(fluidNoHoles1_mesh,fluidHoles1_mesh)
    bafflesFgrade = pv.FGrade(['1'], [green],True)
    bafflesFgrade.set_child(baffles)

#--------------------------------------------------------
#-- Repeating each Bellows Assmbly for N Bellows Stack --
#--------------------------------------------------------
repeatUnion = pv.Union()
repeatUnion.add_child(bellows_fgrade)
repeatUnion.add_child(supportBarrier1_mesh)
if includeBaffles == True:
    repeatUnion.add_child(fluidHoles1_mesh)
    repeatUnion.add_child(bafflesFgrade)
else:
    repeatUnion.add_child(fluidNoHoles1_mesh)

fullStackUnion = pv.Union()
fullStackUnion.add_child(repeatUnion)

for i in range(numStacks-1):
    tempBellowsMesh = repeatUnion
    tempBellowsMesh = pv.Translate(0,0,3.5*(i+1),tempBellowsMesh)
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