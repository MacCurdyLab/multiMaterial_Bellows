import pyvcad as pv

# Materials
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  #agilus
blue = materials.id("blue") #vero
green = materials.id("green") #fluid

#Define Root and SubAssemblies
root = pv.Union()
cappedBellowsStack = pv.Union()

# Dimensions of parts
mainHeight = 3.5   # Dr. Mac's: 3.5[mm]
mainDiameter = 25    # Dr. Mac's: 25[mm]
numStacks = 6
fluidDiameter = 19.66050711

capHeight = 2 #[mm]
capDiameter = 8.5 #[mm]



#---------------------
# Bellows Section
#---------------------

# === Importing bellows Mesh ===
bellowsMesh_single = pv.Mesh(r"MAC_LAB/BellowsTestAssembly/leg_bellows/BellowsStack_noFluid_andrewHeck.STL",red)
bellowsMesh_single = pv.Translate(-24.995731/2-.127134,-mainHeight/2,-24.991465/2-0.124999,bellowsMesh_single)
bellowsMesh_single = pv.Rotate(90,0,0, pv.Vec3(0,0,0),bellowsMesh_single)


# === Creating a stack of bellowsMesh pieces ===
bellowsMesh_stack = pv.Union()
bellowsMesh_stack.add_child(bellowsMesh_single)

for i in range(numStacks-1):
    tempBellowsMesh = bellowsMesh_single
    tempBellowsMesh = pv.Translate(0,0,3.5*(i+1),tempBellowsMesh)
    bellowsMesh_stack.add_child(tempBellowsMesh)

# === MATERIAL GRADING ===
# Gradient Type: gradient4
#
# Stiff Section Settings: 60% Vero, 40% Agilus
# Soft  Section Settings: 15% Vero, 85% Agilus
# Gradient Start / End:   95% → 85%
# Gradient4 Vero/Agilus:  20% / 80%
#
# N (number of Fourier modes) = 80,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
fgrade = pv.FGrade(
    [
        "0.7883483315 -0.0238131345 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.2446783295 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0269613017 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.1184734416 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0026216606 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0500417658 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0146514036 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0034861677 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0117132312 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0351444573 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0216091052 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0060863425 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0146340853 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0196086791 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0151370465 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0037029316 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0104985339 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0063495977 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0037052183 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0020991560 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0043557909 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0021304084 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0050310178 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0022889893 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0001414508 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0047116831 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0070046554 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0022216322 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0018540420 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0028540582 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0032034893 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0006631955 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0015399959 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0004132193 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0020351017 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0015019376 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0004391381 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0024775594 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0045529838 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0023707462 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0006732060 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0024647669 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0031061833 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0010176659 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0015033113 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0011123989 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0004383803 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0015402013 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0018257664 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0003379760 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0031211774 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0032039574 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0013621330 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0011497071 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0032536014 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0026061945 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0001138980 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0013046328 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0013411982 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0002398729 * cos(60*pi ((x^2 + y^2)^0.5)/15) -0.0013309992 * cos(61*pi ((x^2 + y^2)^0.5)/15) -0.0010770104 * cos(62*pi ((x^2 + y^2)^0.5)/15) +0.0008051862 * cos(63*pi ((x^2 + y^2)^0.5)/15) +0.0020276111 * cos(64*pi ((x^2 + y^2)^0.5)/15) +0.0020358599 * cos(65*pi ((x^2 + y^2)^0.5)/15) +0.0006154318 * cos(66*pi ((x^2 + y^2)^0.5)/15) -0.0017023575 * cos(67*pi ((x^2 + y^2)^0.5)/15) -0.0025415213 * cos(68*pi ((x^2 + y^2)^0.5)/15) -0.0014342735 * cos(69*pi ((x^2 + y^2)^0.5)/15) +0.0000475676 * cos(70*pi ((x^2 + y^2)^0.5)/15) +0.0011674004 * cos(71*pi ((x^2 + y^2)^0.5)/15) +0.0011479195 * cos(72*pi ((x^2 + y^2)^0.5)/15) -0.0001048810 * cos(73*pi ((x^2 + y^2)^0.5)/15) -0.0007237074 * cos(74*pi ((x^2 + y^2)^0.5)/15) -0.0000573558 * cos(75*pi ((x^2 + y^2)^0.5)/15) +0.0008437411 * cos(76*pi ((x^2 + y^2)^0.5)/15) +0.0014561532 * cos(77*pi ((x^2 + y^2)^0.5)/15) +0.0009972739 * cos(78*pi ((x^2 + y^2)^0.5)/15) -0.0006901447 * cos(79*pi ((x^2 + y^2)^0.5)/15) -0.0018533361 * cos(80*pi ((x^2 + y^2)^0.5)/15)",
        "0.2116516685 +0.0238131345 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.2446783295 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0269613017 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.1184734416 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0026216606 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0500417658 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0146514036 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0034861677 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0117132312 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0351444573 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0216091052 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0060863425 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0146340853 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0196086791 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0151370465 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0037029316 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0104985339 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0063495977 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0037052183 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0020991560 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0043557909 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0021304084 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0050310178 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0022889893 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0001414508 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0047116831 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0070046554 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0022216322 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0018540420 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0028540582 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0032034893 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0006631955 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0015399959 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0004132193 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0020351017 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0015019376 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0004391381 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0024775594 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0045529838 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0023707462 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0006732060 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0024647669 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0031061833 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0010176659 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0015033113 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0011123989 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0004383803 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0015402013 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0018257664 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0003379760 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0031211774 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0032039574 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0013621330 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0011497071 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0032536014 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0026061945 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0001138980 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0013046328 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0013411982 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0002398729 * cos(60*pi ((x^2 + y^2)^0.5)/15) +0.0013309992 * cos(61*pi ((x^2 + y^2)^0.5)/15) +0.0010770104 * cos(62*pi ((x^2 + y^2)^0.5)/15) -0.0008051862 * cos(63*pi ((x^2 + y^2)^0.5)/15) -0.0020276111 * cos(64*pi ((x^2 + y^2)^0.5)/15) -0.0020358599 * cos(65*pi ((x^2 + y^2)^0.5)/15) -0.0006154318 * cos(66*pi ((x^2 + y^2)^0.5)/15) +0.0017023575 * cos(67*pi ((x^2 + y^2)^0.5)/15) +0.0025415213 * cos(68*pi ((x^2 + y^2)^0.5)/15) +0.0014342735 * cos(69*pi ((x^2 + y^2)^0.5)/15) -0.0000475676 * cos(70*pi ((x^2 + y^2)^0.5)/15) -0.0011674004 * cos(71*pi ((x^2 + y^2)^0.5)/15) -0.0011479195 * cos(72*pi ((x^2 + y^2)^0.5)/15) +0.0001048810 * cos(73*pi ((x^2 + y^2)^0.5)/15) +0.0007237074 * cos(74*pi ((x^2 + y^2)^0.5)/15) +0.0000573558 * cos(75*pi ((x^2 + y^2)^0.5)/15) -0.0008437411 * cos(76*pi ((x^2 + y^2)^0.5)/15) -0.0014561532 * cos(77*pi ((x^2 + y^2)^0.5)/15) -0.0009972739 * cos(78*pi ((x^2 + y^2)^0.5)/15) +0.0006901447 * cos(79*pi ((x^2 + y^2)^0.5)/15) +0.0018533361 * cos(80*pi ((x^2 + y^2)^0.5)/15)"
    ],
    [red, blue],
    True
)

fgrade.set_child(bellowsMesh_stack)

cappedBellowsStack.add_child(fgrade)


#---------------------
# Fluid Section
#---------------------

# Importing fluidMesh
fluidMesh_single = pv.Mesh(r"MAC_LAB/BellowsTestAssembly/leg_bellows/bellowsFluidStack_andrewHeck.STL", green)
#Centering around (0,0,0)
fluidMesh_single = pv.Translate(-fluidDiameter/2-0.098303, -mainHeight/2, -fluidDiameter/2-0.098303, fluidMesh_single)
fluidMesh_single = pv.Rotate(90,0,0, pv.Vec3(0,0,0),fluidMesh_single)

#Creating a stack of the fluidMesh pieces
fluidMesh_stack = pv.Union()
fluidMesh_stack.add_child(fluidMesh_single)

for i in range(numStacks-1):
    tempFluidMesh = fluidMesh_single
    tempFluidMesh = pv.Translate(0,0,3.5*(i+1),tempFluidMesh)
    fluidMesh_stack.add_child(tempFluidMesh)

cappedBellowsStack.add_child(fluidMesh_stack)

#---------------------
# Caps Section
#---------------------
bellows_TopCap = pv.Mesh(r"MAC_LAB/BellowsTestAssembly/leg_bellows/cap_top.STL",blue)
bellows_TopCap = pv.Translate(-0.005538-8.9/2,-5,-.000025-8/2,bellows_TopCap)
bellows_TopCap = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),bellows_TopCap)
bellows_TopCap = pv.Translate(0,0,19.25+5,bellows_TopCap)
cappedBellowsStack.add_child(bellows_TopCap)

bellows_BottomCap = pv.Mesh(r"MAC_LAB/BellowsTestAssembly/leg_bellows/cap.STL",blue)
bellows_BottomCap = pv.Mesh(r"MAC_LAB/BellowsTestAssembly/leg_bellows/cap.STL",blue)
bellows_BottomCap = pv.Translate(-4,-0.5,-4,bellows_BottomCap)
bellows_BottomCap = pv.Rotate(90,0,0,pv.Vec3(0,0,0),bellows_BottomCap)
bellows_BottomCap = pv.Translate(0,0,-2.25,bellows_BottomCap)
cappedBellowsStack.add_child(bellows_BottomCap)



root.add_child(cappedBellowsStack)