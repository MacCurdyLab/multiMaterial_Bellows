# ── DualStackWB_template.py ────────────────────────────────────────────────────────────────
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

#----------------------
#------- SETUP --------
#----------------------

# -- STL Files Location --
stl_Location = "MAC_LAB/STL Files/DualWithBaffles_Intersection"

# -- Materials --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")            # Agilus
blue = materials.id("blue")          # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")        # Support
yellow = materials.id("yellow")      # Air
# note: Housing material is 95% Vero 5% Agilus

#-- Liquid Jetting Percentage --
fluidPercent = 0.725

#-- Dimensions of part --
mainHeight = 21   # Dr. Mac's: 3.5[mm]
mainD = 25    # Dr. Mac's: 25[mm]

#-----------------------------------------------------
#-- Importing meshes ---------------------------------
#-----------------------------------------------------

liquid_mesh = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - VCADTrialAssembly-1 HousingLiquidNB-1.STL", liquid_mat)
baffles_mesh = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - VCADTrialAssembly-1 HousingLiquidWBAssem..Part2^HousingLiquidWBAssemblyVCADTRIAL-1.STL", green
)
liquid_with_holes_mesh = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - VCADTrialAssembly-1 HousingLiquidWBAssemblyVCADTRIAL-2 HousingLiquidWBHoles-1.STL", liquid_mat
)

intersect = pv.Intersection(True)
intersect.add_child(liquid_mesh)
intersect.add_child(baffles_mesh)

fluidUnion = pv.Union()
fluidUnion.add_child(liquid_with_holes_mesh)

# gradient stuff
x = 39.5 + 0.105001
y = 22 + 0.01
z = 56.794621

# -- Importing First Baffles Mesh Mesh --
bellows1 = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - BellowsGradientAssemblyCentered-1.STL", red)
bellows1 = pv.Translate(-x, -y, 0, bellows1)


# Use the computed Fourier‐series strings in the call below:
fgrade1 = pv.FGrade(
    [
        "{{agilus_string}}",
        "{{vero_string}}"
    ],
    [red, blue],
    True
)

fgrade1.set_child(bellows1)

# Translate into position:
translate1 = pv.Translate(x, y, 0)
translate1.set_child(fgrade1)


#-- Second Mesh for Bellows (same settings) --
bellows2 = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - BellowsGradientAssemblyCentered-2.STL", red)
bellows2 = pv.Translate(-37-x, -y, 0, bellows2)
fgrade2 = pv.FGrade(
    [
        "{{agilus_string}}",
        "{{vero_string}}"
    ],
    [red, blue],
    True
)

fgrade2.set_child(bellows2)

#Translate into correct position:
translate2 = pv.Translate(37+x, y, 0)
translate2.set_child(fgrade2)


#-- Importing housing structure --
housing_mesh = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - HousingAssemblyDual-1.STL", blue)
# Applying 95% vero 5% Agilus grade to structural parts
housing_fgrade = pv.FGrade(
    ["0.95", "0.05"], [blue, red], True
)
housing_fgrade.set_child(housing_mesh)

#-- Importing liquid part of the bellows structure --
liquid_bellows1 = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - LiquidBellowsWBAssembly-1 LiquidAssemblyWB-1.STL", liquid_mat)
fluidUnion.add_child(liquid_bellows1)

baffles1 = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - LiquidBellowsWBAssembly-1 Part1^LiquidBellowsWBAssembly-1.STL", green
)

liquid_bellows2 = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - LiquidBellowsWBAssembly-2 LiquidAssemblyWB-1.STL", liquid_mat
)
fluidUnion.add_child(liquid_bellows2)

baffles2 = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - LiquidBellowsWBAssembly-2 Part1^LiquidBellowsWBAssembly-1.STL", green
)

#-- Importing support structures --
support1_mesh = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - SupportBellowsAssembly-1.STL", green)
support2_mesh = pv.Mesh(
    stl_Location+"/AssemblyWithBaffles_usingIntersection - SupportBellowsAssembly-2.STL", green)

#-- Setting Fluid Gradient --
fluidAir_fgrade =  pv.FGrade([str(fluidPercent),str(1-fluidPercent)],[liquid_mat,yellow],True)
fluidAir_fgrade.set_child(fluidUnion)

#--------------------------
#---Setting Root Node------
#--------------------------
root = pv.Union()
root.add_child(intersect)
root.add_child(translate1)
root.add_child(translate2)
root.add_child(baffles1)
root.add_child(baffles2)
root.add_child(housing_fgrade)
root.add_child(support1_mesh)
root.add_child(support2_mesh)
root.add_child(fluidAir_fgrade)