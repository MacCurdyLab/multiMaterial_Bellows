# Variable_Dual_Stack_w_Baffles.py
import pyvcad as pv

# === MATERIAL GRADING ===
# Gradient Type: gradient3
# Design Type: Dual assembly with baffles
# Stiff Section Settings: 70% Vero, 30% Agilus
# Soft  Section Settings: 40% Vero, 60% Agilus
# Gradient Start / End:   65% → 60%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 85,  L = 15

# ----------------------
# ------- SETUP --------
# ----------------------

# -- STL Files Location --
stl_Location = "MAC_LAB/STL Files/DualWithBaffles/LOWRES"

# -- Materials --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")            # Agilus
blue = materials.id("blue")          # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")        # Support
yellow = materials.id("yellow")      # Air
# note: Housing material is 95% Vero 5% Agilus

# -- Liquid Jetting Percentage --
fluidPercent = 0.725

# -- Dimensions of part --
mainHeight = 21   
height = 3.5   # Dr. Mac's: 3.5[mm]
mainD = 25    # Dr. Mac's: 25[mm]

# -- Stack Settings --
fluidPercent = 0.725
numStacks = 6
includeBaffles = True

# gradient stuff
x = 53.507790 + mainD/2
y = 8.500941 +mainD/2
z = 9.0

#Defining Root Node
root = pv.Union()

# Turning Baffles on/off
includeBaffles = True

# -----------------------------------------------------
# -- Importing meshes ---------------------------------
# -----------------------------------------------------
# Top Bellows = 1
# Bottom Bellows = 6
# Top liquid = 7
# Bottom liquid = 9
# Top Support = 4
# Bottom Support = 6

#agilus = "0.5388888889 -0.0194761451 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.1667828292 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0287682742 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.0705436096 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0113495337 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0101949280 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0013944314 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0100675187 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0070248311 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0059124818 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0029796506 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0010670497 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0033633039 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0022722648 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0035036902 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0003291048 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0008245263 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0005182850 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0026758090 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0005722107 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0000338768 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0015065208 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0004994719 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0010161242 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0001990851 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0005409934 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0006242889 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0008534110 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0005203779 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0000032637 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0004003381 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0004658342 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0006966719 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0001303944 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0000299534 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0001455797 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0006350515 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0000278583 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0002734324 * cos(40*pi ((x^2 + y^2)^0.5)/15) -0.0000247783 * cos(41*pi ((x^2 + y^2)^0.5)/15) -0.0004029194 * cos(42*pi ((x^2 + y^2)^0.5)/15) -0.0001158816 * cos(43*pi ((x^2 + y^2)^0.5)/15) +0.0003935225 * cos(44*pi ((x^2 + y^2)^0.5)/15) +0.0000817699 * cos(45*pi ((x^2 + y^2)^0.5)/15) +0.0001383446 * cos(46*pi ((x^2 + y^2)^0.5)/15) +0.0001694962 * cos(47*pi ((x^2 + y^2)^0.5)/15) -0.0003367746 * cos(48*pi ((x^2 + y^2)^0.5)/15) -0.0002070919 * cos(49*pi ((x^2 + y^2)^0.5)/15) +0.0000403404 * cos(50*pi ((x^2 + y^2)^0.5)/15) -0.0001022512 * cos(51*pi ((x^2 + y^2)^0.5)/15) +0.0001925643 * cos(52*pi ((x^2 + y^2)^0.5)/15) +0.0002878415 * cos(53*pi ((x^2 + y^2)^0.5)/15) -0.0000888688 * cos(54*pi ((x^2 + y^2)^0.5)/15) -0.0000344357 * cos(55*pi ((x^2 + y^2)^0.5)/15) -0.0000650408 * cos(56*pi ((x^2 + y^2)^0.5)/15) -0.0002684086 * cos(57*pi ((x^2 + y^2)^0.5)/15) +0.0000402386 * cos(58*pi ((x^2 + y^2)^0.5)/15) +0.0001586868 * cos(59*pi ((x^2 + y^2)^0.5)/15) +0.0000164178 * cos(60*pi ((x^2 + y^2)^0.5)/15) +0.0001651334 * cos(61*pi ((x^2 + y^2)^0.5)/15) +0.0000321951 * cos(62*pi ((x^2 + y^2)^0.5)/15) -0.0002108903 * cos(63*pi ((x^2 + y^2)^0.5)/15) -0.0000463377 * cos(64*pi ((x^2 + y^2)^0.5)/15) -0.0000393184 * cos(65*pi ((x^2 + y^2)^0.5)/15) -0.0000638979 * cos(66*pi ((x^2 + y^2)^0.5)/15) +0.0001816128 * cos(67*pi ((x^2 + y^2)^0.5)/15) +0.0001087606 * cos(68*pi ((x^2 + y^2)^0.5)/15) -0.0000473908 * cos(69*pi ((x^2 + y^2)^0.5)/15) +0.0000323946 * cos(70*pi ((x^2 + y^2)^0.5)/15) -0.0001062718 * cos(71*pi ((x^2 + y^2)^0.5)/15) -0.0001489061 * cos(72*pi ((x^2 + y^2)^0.5)/15) +0.0000675603 * cos(73*pi ((x^2 + y^2)^0.5)/15) +0.0000397398 * cos(74*pi ((x^2 + y^2)^0.5)/15) +0.0000365161 * cos(75*pi ((x^2 + y^2)^0.5)/15) +0.0001364163 * cos(76*pi ((x^2 + y^2)^0.5)/15) -0.0000360147 * cos(77*pi ((x^2 + y^2)^0.5)/15) -0.0001076065 * cos(78*pi ((x^2 + y^2)^0.5)/15) -0.0000083713 * cos(79*pi ((x^2 + y^2)^0.5)/15) -0.0000778679 * cos(80*pi ((x^2 + y^2)^0.5)/15) -0.0000074486 * cos(81*pi ((x^2 + y^2)^0.5)/15) +0.0001348073 * cos(82*pi ((x^2 + y^2)^0.5)/15) +0.0000251890 * cos(83*pi ((x^2 + y^2)^0.5)/15) +0.0000060556 * cos(84*pi ((x^2 + y^2)^0.5)/15) +0.0000259557 * cos(85*pi ((x^2 + y^2)^0.5)/15)"
#vero = "0.4611111111 +0.0194761451 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.1667828292 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0287682742 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.0705436096 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0113495337 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0101949280 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0013944314 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0100675187 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0070248311 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0059124818 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0029796506 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0010670497 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0033633039 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0022722648 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0035036902 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0003291048 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0008245263 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0005182850 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0026758090 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0005722107 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0000338768 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0015065208 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0004994719 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0010161242 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0001990851 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0005409934 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0006242889 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0008534110 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0005203779 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0000032637 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0004003381 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0004658342 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0006966719 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0001303944 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0000299534 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0001455797 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0006350515 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0000278583 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0002734324 * cos(40*pi ((x^2 + y^2)^0.5)/15) +0.0000247783 * cos(41*pi ((x^2 + y^2)^0.5)/15) +0.0004029194 * cos(42*pi ((x^2 + y^2)^0.5)/15) +0.0001158816 * cos(43*pi ((x^2 + y^2)^0.5)/15) -0.0003935225 * cos(44*pi ((x^2 + y^2)^0.5)/15) -0.0000817699 * cos(45*pi ((x^2 + y^2)^0.5)/15) -0.0001383446 * cos(46*pi ((x^2 + y^2)^0.5)/15) -0.0001694962 * cos(47*pi ((x^2 + y^2)^0.5)/15) +0.0003367746 * cos(48*pi ((x^2 + y^2)^0.5)/15) +0.0002070919 * cos(49*pi ((x^2 + y^2)^0.5)/15) -0.0000403404 * cos(50*pi ((x^2 + y^2)^0.5)/15) +0.0001022512 * cos(51*pi ((x^2 + y^2)^0.5)/15) -0.0001925643 * cos(52*pi ((x^2 + y^2)^0.5)/15) -0.0002878415 * cos(53*pi ((x^2 + y^2)^0.5)/15) +0.0000888688 * cos(54*pi ((x^2 + y^2)^0.5)/15) +0.0000344357 * cos(55*pi ((x^2 + y^2)^0.5)/15) +0.0000650408 * cos(56*pi ((x^2 + y^2)^0.5)/15) +0.0002684086 * cos(57*pi ((x^2 + y^2)^0.5)/15) -0.0000402386 * cos(58*pi ((x^2 + y^2)^0.5)/15) -0.0001586868 * cos(59*pi ((x^2 + y^2)^0.5)/15) -0.0000164178 * cos(60*pi ((x^2 + y^2)^0.5)/15) -0.0001651334 * cos(61*pi ((x^2 + y^2)^0.5)/15) -0.0000321951 * cos(62*pi ((x^2 + y^2)^0.5)/15) +0.0002108903 * cos(63*pi ((x^2 + y^2)^0.5)/15) +0.0000463377 * cos(64*pi ((x^2 + y^2)^0.5)/15) +0.0000393184 * cos(65*pi ((x^2 + y^2)^0.5)/15) +0.0000638979 * cos(66*pi ((x^2 + y^2)^0.5)/15) -0.0001816128 * cos(67*pi ((x^2 + y^2)^0.5)/15) -0.0001087606 * cos(68*pi ((x^2 + y^2)^0.5)/15) +0.0000473908 * cos(69*pi ((x^2 + y^2)^0.5)/15) -0.0000323946 * cos(70*pi ((x^2 + y^2)^0.5)/15) +0.0001062718 * cos(71*pi ((x^2 + y^2)^0.5)/15) +0.0001489061 * cos(72*pi ((x^2 + y^2)^0.5)/15) -0.0000675603 * cos(73*pi ((x^2 + y^2)^0.5)/15) -0.0000397398 * cos(74*pi ((x^2 + y^2)^0.5)/15) -0.0000365161 * cos(75*pi ((x^2 + y^2)^0.5)/15) -0.0001364163 * cos(76*pi ((x^2 + y^2)^0.5)/15) +0.0000360147 * cos(77*pi ((x^2 + y^2)^0.5)/15) +0.0001076065 * cos(78*pi ((x^2 + y^2)^0.5)/15) +0.0000083713 * cos(79*pi ((x^2 + y^2)^0.5)/15) +0.0000778679 * cos(80*pi ((x^2 + y^2)^0.5)/15) +0.0000074486 * cos(81*pi ((x^2 + y^2)^0.5)/15) -0.0001348073 * cos(82*pi ((x^2 + y^2)^0.5)/15) -0.0000251890 * cos(83*pi ((x^2 + y^2)^0.5)/15) -0.0000060556 * cos(84*pi ((x^2 + y^2)^0.5)/15) -0.0000259557 * cos(85*pi ((x^2 + y^2)^0.5)/15)"
agilus = "0.5"
vero = agilus

# Stack 1 Bellows Meshes
# Bellows1 Mesh
bellows1 = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - Variable Bellows 6 Stack-1 Variable_Bellow-6.STL", red)
bellows1 = pv.Translate(-x, -y, 0, bellows1)
fgrade1 = pv.FGrade(
    [
        agilus,
        vero
    ],
    [red, blue],
    True
)
fgrade1.set_child(bellows1)
# Translate into position:
translate1 = pv.Translate(x, y, 0)
translate1.set_child(fgrade1)

fluid_fgrade = pv.FGrade([str(fluidPercent), str(
    1-fluidPercent)], [liquid_mat, yellow], True)
fluid_NoHoles = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - Variable Bellows 6 Stack-1 Variable_Fluid-9.STL", liquid_mat)

if includeBaffles:
    fluid_Holes = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - Variable Bellows 6 Stack-1 Variable_Fluid-9.STL", liquid_mat)

    baffles = pv.Difference(fluid_NoHoles, fluid_Holes)
    bafflesFgrade = pv.FGrade(['1'], [green], True)
    bafflesFgrade.set_child(baffles)
    fluid_fgrade.set_child(fluid_Holes)
else:
    fluid_fgrade.set_child(fluid_NoHoles)

support = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - Variable Bellows 6 Stack-1 Variable_SupportBundary-6.STL", green)

# -- Repeating each Bellows Assmbly for N Bellows Stack --
# --------------------------------------------------------
repeatUnion = pv.Union()
repeatUnion.add_child(translate1)
repeatUnion.add_child(support)
repeatUnion.add_child(fluid_fgrade)

if includeBaffles:
    repeatUnion.add_child(bafflesFgrade)

# Union node for the entire stack of bellows
fullStackUnion = pv.Union()
fullStackUnion.add_child(repeatUnion)

for i in range(numStacks-1):
    #tempBellowsMesh = repeatUnion.clone()
    #tempBellowsMesh = pv.Translate(0, 0, height*(i+1), tempBellowsMesh)
    #fullStackUnion.add_child(tempBellowsMesh)

    repeatUnion = pv.Translate(0, 0, height, repeatUnion)
    fullStackUnion.add_child(repeatUnion)


# Stack 2
fullStackUnion2 = fullStackUnion.clone()
fullStackUnion2 = pv.Translate(-37,0,0,fullStackUnion2)

# -- Importing housing structure --
housing_mesh = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - HousingAssemblyDual-1.STL", blue,True)
# Applying 95% vero 5% Agilus grade to structural parts
housing_fgrade = pv.FGrade(
    ["0.95", "0.05"], [blue, red], True
)
housing_fgrade.set_child(housing_mesh)

liquid_mesh = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - VCADTrialAssembly-1 HousingLiquidNB-1.STL", liquid_mat)
baffles_mesh = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - VCADTrialAssembly-1 HousingLiquidWBAssem__Part2^HousingLiquidWBAssemblyVCADTRIAL-1.STL", green
)

#Air-Fluid Fgrade for fluid in piping
pipeFluid_FGrade = pv.FGrade([str(fluidPercent), str(1-fluidPercent)], [liquid_mat, yellow], True)

if includeBaffles:
    liquid_with_holes_mesh = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - VCADTrialAssembly-1 HousingLiquidWBAssemblyVCADTRIAL-2 HousingLiquidWBHoles-1.STL", liquid_mat
    )

    intersect = pv.Intersection(True)
    intersect.add_child(liquid_mesh)
    intersect.add_child(baffles_mesh)
    root.add_child(intersect)
    pipeFluid_FGrade.set_child(liquid_with_holes_mesh)
else:
    pipeFluid_FGrade.set_child(liquid_mesh)

# -- Adding all Parts to ROOT Union --
root.add_child(pipeFluid_FGrade)
root.add_child(fullStackUnion)
root.add_child(fullStackUnion2)
root.add_child(housing_fgrade)