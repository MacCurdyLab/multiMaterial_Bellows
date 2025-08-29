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
# Design Type: Single stack with baffles
# Stiff Section Settings: 50% Vero, 50% Agilus
# Soft  Section Settings: 15% Vero, 85% Agilus
# Gradient Start / End:   85% → 85%
# Gradient4 Vero/Agilus:  20% / 80%
#
# N (number of Fourier modes) = 80,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
        "0.7644444444 -0.0086616901 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.1486373491 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0195826117 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.0938169373 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0169143274 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0352244515 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0049407842 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0024587218 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0054283650 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0127692733 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0068982228 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0062941064 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0013465654 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0019316055 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0038368150 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0040475817 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0037325381 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0014310253 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0001399168 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0011125808 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0029030898 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0012825719 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0019926052 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0001994234 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0007794131 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0003749563 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0020918477 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0001832766 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0009085065 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0009513363 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0001477910 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0013746579 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0001973190 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0002573395 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0001309430 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0008512651 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0004355699 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0007893773 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0002236112 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0000730545 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0003203235 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0006166149 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0005187628 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0003673446 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0000929290 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0001731912 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0004511444 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0003511912 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0004549281 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0001144295 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0000720085 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0001292674 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0004850154 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0001268067 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0003118446 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0000094140 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0001985860 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0000198850 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0004298474 * cos(60*pi ((x^2 + y^2)^0.5)/15) +0.0000179162 * cos(61*pi ((x^2 + y^2)^0.5)/15) -0.0001525978 * cos(62*pi ((x^2 + y^2)^0.5)/15) +0.0000112013 * cos(63*pi ((x^2 + y^2)^0.5)/15) -0.0002547206 * cos(64*pi ((x^2 + y^2)^0.5)/15) -0.0000922205 * cos(65*pi ((x^2 + y^2)^0.5)/15) +0.0003185763 * cos(66*pi ((x^2 + y^2)^0.5)/15) +0.0000752563 * cos(67*pi ((x^2 + y^2)^0.5)/15) -0.0000241936 * cos(68*pi ((x^2 + y^2)^0.5)/15) +0.0000702987 * cos(69*pi ((x^2 + y^2)^0.5)/15) -0.0002402465 * cos(70*pi ((x^2 + y^2)^0.5)/15) -0.0001667464 * cos(71*pi ((x^2 + y^2)^0.5)/15) +0.0001919512 * cos(72*pi ((x^2 + y^2)^0.5)/15) +0.0000614319 * cos(73*pi ((x^2 + y^2)^0.5)/15) +0.0000484818 * cos(74*pi ((x^2 + y^2)^0.5)/15) +0.0001407355 * cos(75*pi ((x^2 + y^2)^0.5)/15) -0.0001762012 * cos(76*pi ((x^2 + y^2)^0.5)/15) -0.0001877216 * cos(77*pi ((x^2 + y^2)^0.5)/15) +0.0000851827 * cos(78*pi ((x^2 + y^2)^0.5)/15) +0.0000063192 * cos(79*pi ((x^2 + y^2)^0.5)/15) +0.0000627195 * cos(80*pi ((x^2 + y^2)^0.5)/15)",
        "0.2355555556 +0.0086616901 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.1486373491 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0195826117 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.0938169373 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0169143274 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0352244515 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0049407842 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0024587218 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0054283650 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0127692733 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0068982228 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0062941064 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0013465654 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0019316055 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0038368150 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0040475817 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0037325381 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0014310253 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0001399168 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0011125808 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0029030898 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0012825719 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0019926052 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0001994234 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0007794131 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0003749563 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0020918477 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0001832766 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0009085065 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0009513363 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0001477910 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0013746579 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0001973190 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0002573395 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0001309430 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0008512651 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0004355699 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0007893773 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0002236112 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0000730545 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0003203235 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0006166149 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0005187628 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0003673446 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0000929290 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0001731912 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0004511444 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0003511912 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0004549281 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0001144295 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0000720085 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0001292674 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0004850154 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0001268067 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0003118446 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0000094140 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0001985860 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0000198850 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0004298474 * cos(60*pi ((x^2 + y^2)^0.5)/15) -0.0000179162 * cos(61*pi ((x^2 + y^2)^0.5)/15) +0.0001525978 * cos(62*pi ((x^2 + y^2)^0.5)/15) -0.0000112013 * cos(63*pi ((x^2 + y^2)^0.5)/15) +0.0002547206 * cos(64*pi ((x^2 + y^2)^0.5)/15) +0.0000922205 * cos(65*pi ((x^2 + y^2)^0.5)/15) -0.0003185763 * cos(66*pi ((x^2 + y^2)^0.5)/15) -0.0000752563 * cos(67*pi ((x^2 + y^2)^0.5)/15) +0.0000241936 * cos(68*pi ((x^2 + y^2)^0.5)/15) -0.0000702987 * cos(69*pi ((x^2 + y^2)^0.5)/15) +0.0002402465 * cos(70*pi ((x^2 + y^2)^0.5)/15) +0.0001667464 * cos(71*pi ((x^2 + y^2)^0.5)/15) -0.0001919512 * cos(72*pi ((x^2 + y^2)^0.5)/15) -0.0000614319 * cos(73*pi ((x^2 + y^2)^0.5)/15) -0.0000484818 * cos(74*pi ((x^2 + y^2)^0.5)/15) -0.0001407355 * cos(75*pi ((x^2 + y^2)^0.5)/15) +0.0001762012 * cos(76*pi ((x^2 + y^2)^0.5)/15) +0.0001877216 * cos(77*pi ((x^2 + y^2)^0.5)/15) -0.0000851827 * cos(78*pi ((x^2 + y^2)^0.5)/15) -0.0000063192 * cos(79*pi ((x^2 + y^2)^0.5)/15) -0.0000627195 * cos(80*pi ((x^2 + y^2)^0.5)/15)"
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
