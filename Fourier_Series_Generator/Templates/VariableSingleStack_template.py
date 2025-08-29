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
# Gradient Type: {{gradient_type}}
# Design Type: {{design}}
# Stiff Section Settings: {{vero_stiff_section}}% Vero, {{agilus_stiff_section}}% Agilus
# Soft  Section Settings: {{vero_soft_section}}% Vero, {{agilus_soft_section}}% Agilus
# Gradient Start / End:   {{gradient_start}}% → {{gradient_end}}%
# Gradient4 Vero/Agilus:  {{gradient4_vero}}% / {{gradient4_agilus}}%
#
# N (number of Fourier modes) = {{N}},  L = {{L}}
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "{{agilus_string}}",
          "{{vero_string}}"
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