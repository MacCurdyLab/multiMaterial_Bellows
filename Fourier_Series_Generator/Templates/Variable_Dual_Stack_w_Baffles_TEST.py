# Variable_Dual_Stack_w_Baffles.py
import pyvcad as pv

# === MATERIAL GRADING ===
# Gradient Type: {{gradient_type}}
# Design Type: {{design}}
# Stiff Section Settings: {{vero_stiff_section}}% Vero, {{agilus_stiff_section}}% Agilus
# Soft  Section Settings: {{vero_soft_section}}% Vero, {{agilus_soft_section}}% Agilus
# Gradient Start / End:   {{gradient_start}}% → {{gradient_end}}%
# Gradient4 Vero/Agilus:  {{gradient4_vero}}% / {{gradient4_agilus}}%
#
# N (number of Fourier modes) = {{N}},  L = {{L}}

# ----------------------
# ------- SETUP --------
# ----------------------

# -- STL Files Location --
stl_Location = "../STL Files/DualWithBaffles/LOWRES"

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

agilus = "{{agilus_string}}"
vero = "{{vero_string}}"

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
    root.add_child(intersect) # adding baffles to root
    pipeFluid_FGrade.set_child(liquid_with_holes_mesh)
else:
    pipeFluid_FGrade.set_child(liquid_mesh)

# -- Adding all Parts to ROOT Union --
root.add_child(pipeFluid_FGrade)
root.add_child(fullStackUnion)
root.add_child(fullStackUnion2)
root.add_child(housing_fgrade)