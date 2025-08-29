# ── SinglStackWB.py ────────────────────────────────────────────────────────────────
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
mainHeight = 3.5   # Dr. Mac's: 3.5[mm]
mainD = 29    # Dr. Mac's: 25[mm]
capHeight = 1 #[mm]

#-- Stack Settings --
numStacks = 3
includeBaffles = False

#-- placing stuff --
x = 5.265812
y = 5.265812
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
# Gradient Type: gradient3
# Design Type: Single stack
# Stiff Section Settings: 70% Vero, 30% Agilus
# Soft  Section Settings: 50% Vero, 50% Agilus
# Gradient Start / End:   85% → 50%
# Gradient4 Vero/Agilus:  20% / 80%
#
# N (number of Fourier modes) = 80,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.6183333333 -0.0464141830 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.2874931731 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0325339459 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.0517031571 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0211066513 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0155043791 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0036909822 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0122019208 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0056472795 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0016870840 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0020140489 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0036045654 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0002852456 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0014307286 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0009599198 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0002282898 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0013160275 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0014399636 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0000539197 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0008694786 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0010329237 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0004930318 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0005775266 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0007208625 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0001653134 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0002611215 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0004985451 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0001451762 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0004250098 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0004202953 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0001002427 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0002597929 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0004585059 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0001574707 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0002259137 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0002804049 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0001380836 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0001382954 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0002706563 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0000542350 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0001676715 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0002101691 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0000950290 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0001505491 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0002337275 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0000704034 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0000952616 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0001707061 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0000907037 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0000993935 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0001457845 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0000387774 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0000791462 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0001440302 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0000578858 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0000971919 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0001277830 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0000540121 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0000546924 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0001221313 * cos(60*pi ((x^2 + y^2)^0.5)/15) +0.0000490783 * cos(61*pi ((x^2 + y^2)^0.5)/15) +0.0000635187 * cos(62*pi ((x^2 + y^2)^0.5)/15) -0.0000876143 * cos(63*pi ((x^2 + y^2)^0.5)/15) +0.0000398653 * cos(64*pi ((x^2 + y^2)^0.5)/15) +0.0000542828 * cos(65*pi ((x^2 + y^2)^0.5)/15) -0.0001021839 * cos(66*pi ((x^2 + y^2)^0.5)/15) +0.0000307585 * cos(67*pi ((x^2 + y^2)^0.5)/15) +0.0000570781 * cos(68*pi ((x^2 + y^2)^0.5)/15) -0.0000839313 * cos(69*pi ((x^2 + y^2)^0.5)/15) +0.0000460594 * cos(70*pi ((x^2 + y^2)^0.5)/15) +0.0000447949 * cos(71*pi ((x^2 + y^2)^0.5)/15) -0.0000839552 * cos(72*pi ((x^2 + y^2)^0.5)/15) +0.0000286458 * cos(73*pi ((x^2 + y^2)^0.5)/15) +0.0000362876 * cos(74*pi ((x^2 + y^2)^0.5)/15) -0.0000658439 * cos(75*pi ((x^2 + y^2)^0.5)/15) +0.0000334745 * cos(76*pi ((x^2 + y^2)^0.5)/15) +0.0000448746 * cos(77*pi ((x^2 + y^2)^0.5)/15) -0.0000682048 * cos(78*pi ((x^2 + y^2)^0.5)/15) +0.0000219383 * cos(79*pi ((x^2 + y^2)^0.5)/15) +0.0000339506 * cos(80*pi ((x^2 + y^2)^0.5)/15)",
          "0.3816666667 +0.0464141830 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.2874931731 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0325339459 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.0517031571 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0211066513 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0155043791 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0036909822 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0122019208 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0056472795 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0016870840 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0020140489 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0036045654 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0002852456 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0014307286 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0009599198 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0002282898 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0013160275 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0014399636 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0000539197 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0008694786 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0010329237 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0004930318 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0005775266 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0007208625 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0001653134 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0002611215 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0004985451 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0001451762 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0004250098 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0004202953 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0001002427 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0002597929 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0004585059 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0001574707 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0002259137 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0002804049 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0001380836 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0001382954 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0002706563 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0000542350 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0001676715 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0002101691 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0000950290 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0001505491 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0002337275 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0000704034 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0000952616 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0001707061 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0000907037 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0000993935 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0001457845 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0000387774 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0000791462 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0001440302 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0000578858 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0000971919 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0001277830 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0000540121 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0000546924 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0001221313 * cos(60*pi ((x^2 + y^2)^0.5)/15) -0.0000490783 * cos(61*pi ((x^2 + y^2)^0.5)/15) -0.0000635187 * cos(62*pi ((x^2 + y^2)^0.5)/15) +0.0000876143 * cos(63*pi ((x^2 + y^2)^0.5)/15) -0.0000398653 * cos(64*pi ((x^2 + y^2)^0.5)/15) -0.0000542828 * cos(65*pi ((x^2 + y^2)^0.5)/15) +0.0001021839 * cos(66*pi ((x^2 + y^2)^0.5)/15) -0.0000307585 * cos(67*pi ((x^2 + y^2)^0.5)/15) -0.0000570781 * cos(68*pi ((x^2 + y^2)^0.5)/15) +0.0000839313 * cos(69*pi ((x^2 + y^2)^0.5)/15) -0.0000460594 * cos(70*pi ((x^2 + y^2)^0.5)/15) -0.0000447949 * cos(71*pi ((x^2 + y^2)^0.5)/15) +0.0000839552 * cos(72*pi ((x^2 + y^2)^0.5)/15) -0.0000286458 * cos(73*pi ((x^2 + y^2)^0.5)/15) -0.0000362876 * cos(74*pi ((x^2 + y^2)^0.5)/15) +0.0000658439 * cos(75*pi ((x^2 + y^2)^0.5)/15) -0.0000334745 * cos(76*pi ((x^2 + y^2)^0.5)/15) -0.0000448746 * cos(77*pi ((x^2 + y^2)^0.5)/15) +0.0000682048 * cos(78*pi ((x^2 + y^2)^0.5)/15) -0.0000219383 * cos(79*pi ((x^2 + y^2)^0.5)/15) -0.0000339506 * cos(80*pi ((x^2 + y^2)^0.5)/15)"
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

cap2_mesh = cap1fgrade
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