# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/Diameter_25mm--WallThick_1-1mm"

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
includeBaffles = False
fluidPercent = 0.725

#-- placing stuff --
x = 0
y = 0
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
# Soft  Section Settings: 10% Vero, 90% Agilus
# Gradient Start / End:   95% → 90%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 40,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [
          "0.7555555556 -0.0320010068 * cos(1*pi ((x^2 + y^2)^0.5)/15) +0.3048636432 * cos(2*pi ((x^2 + y^2)^0.5)/15) +0.0545999234 * cos(3*pi ((x^2 + y^2)^0.5)/15) -0.1438798634 * cos(4*pi ((x^2 + y^2)^0.5)/15) -0.0283510676 * cos(5*pi ((x^2 + y^2)^0.5)/15) +0.0254206394 * cos(6*pi ((x^2 + y^2)^0.5)/15) -0.0024632750 * cos(7*pi ((x^2 + y^2)^0.5)/15) +0.0198852769 * cos(8*pi ((x^2 + y^2)^0.5)/15) +0.0162790708 * cos(9*pi ((x^2 + y^2)^0.5)/15) -0.0135583616 * cos(10*pi ((x^2 + y^2)^0.5)/15) -0.0066367364 * cos(11*pi ((x^2 + y^2)^0.5)/15) -0.0016736729 * cos(12*pi ((x^2 + y^2)^0.5)/15) -0.0074973133 * cos(13*pi ((x^2 + y^2)^0.5)/15) +0.0049601143 * cos(14*pi ((x^2 + y^2)^0.5)/15) +0.0077448010 * cos(15*pi ((x^2 + y^2)^0.5)/15) -0.0009170600 * cos(16*pi ((x^2 + y^2)^0.5)/15) +0.0016870758 * cos(17*pi ((x^2 + y^2)^0.5)/15) -0.0009506075 * cos(18*pi ((x^2 + y^2)^0.5)/15) -0.0059053952 * cos(19*pi ((x^2 + y^2)^0.5)/15) -0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) +0.0014045965 * cos(21*pi ((x^2 + y^2)^0.5)/15) -0.0000890728 * cos(22*pi ((x^2 + y^2)^0.5)/15) +0.0032954246 * cos(23*pi ((x^2 + y^2)^0.5)/15) +0.0011256713 * cos(24*pi ((x^2 + y^2)^0.5)/15) -0.0023207778 * cos(25*pi ((x^2 + y^2)^0.5)/15) -0.0003574744 * cos(26*pi ((x^2 + y^2)^0.5)/15) -0.0011347994 * cos(27*pi ((x^2 + y^2)^0.5)/15) -0.0014060195 * cos(28*pi ((x^2 + y^2)^0.5)/15) +0.0018924885 * cos(29*pi ((x^2 + y^2)^0.5)/15) +0.0011358079 * cos(30*pi ((x^2 + y^2)^0.5)/15) -0.0000611516 * cos(31*pi ((x^2 + y^2)^0.5)/15) +0.0008995539 * cos(32*pi ((x^2 + y^2)^0.5)/15) -0.0009931555 * cos(33*pi ((x^2 + y^2)^0.5)/15) -0.0015552078 * cos(34*pi ((x^2 + y^2)^0.5)/15) +0.0003397407 * cos(35*pi ((x^2 + y^2)^0.5)/15) -0.0000663066 * cos(36*pi ((x^2 + y^2)^0.5)/15) +0.0002732666 * cos(37*pi ((x^2 + y^2)^0.5)/15) +0.0014145282 * cos(38*pi ((x^2 + y^2)^0.5)/15) -0.0000825822 * cos(39*pi ((x^2 + y^2)^0.5)/15) -0.0006140566 * cos(40*pi ((x^2 + y^2)^0.5)/15)",
          "0.2444444444 +0.0320010068 * cos(1*pi ((x^2 + y^2)^0.5)/15) -0.3048636432 * cos(2*pi ((x^2 + y^2)^0.5)/15) -0.0545999234 * cos(3*pi ((x^2 + y^2)^0.5)/15) +0.1438798634 * cos(4*pi ((x^2 + y^2)^0.5)/15) +0.0283510676 * cos(5*pi ((x^2 + y^2)^0.5)/15) -0.0254206394 * cos(6*pi ((x^2 + y^2)^0.5)/15) +0.0024632750 * cos(7*pi ((x^2 + y^2)^0.5)/15) -0.0198852769 * cos(8*pi ((x^2 + y^2)^0.5)/15) -0.0162790708 * cos(9*pi ((x^2 + y^2)^0.5)/15) +0.0135583616 * cos(10*pi ((x^2 + y^2)^0.5)/15) +0.0066367364 * cos(11*pi ((x^2 + y^2)^0.5)/15) +0.0016736729 * cos(12*pi ((x^2 + y^2)^0.5)/15) +0.0074973133 * cos(13*pi ((x^2 + y^2)^0.5)/15) -0.0049601143 * cos(14*pi ((x^2 + y^2)^0.5)/15) -0.0077448010 * cos(15*pi ((x^2 + y^2)^0.5)/15) +0.0009170600 * cos(16*pi ((x^2 + y^2)^0.5)/15) -0.0016870758 * cos(17*pi ((x^2 + y^2)^0.5)/15) +0.0009506075 * cos(18*pi ((x^2 + y^2)^0.5)/15) +0.0059053952 * cos(19*pi ((x^2 + y^2)^0.5)/15) +0.0000216313 * cos(20*pi ((x^2 + y^2)^0.5)/15) -0.0014045965 * cos(21*pi ((x^2 + y^2)^0.5)/15) +0.0000890728 * cos(22*pi ((x^2 + y^2)^0.5)/15) -0.0032954246 * cos(23*pi ((x^2 + y^2)^0.5)/15) -0.0011256713 * cos(24*pi ((x^2 + y^2)^0.5)/15) +0.0023207778 * cos(25*pi ((x^2 + y^2)^0.5)/15) +0.0003574744 * cos(26*pi ((x^2 + y^2)^0.5)/15) +0.0011347994 * cos(27*pi ((x^2 + y^2)^0.5)/15) +0.0014060195 * cos(28*pi ((x^2 + y^2)^0.5)/15) -0.0018924885 * cos(29*pi ((x^2 + y^2)^0.5)/15) -0.0011358079 * cos(30*pi ((x^2 + y^2)^0.5)/15) +0.0000611516 * cos(31*pi ((x^2 + y^2)^0.5)/15) -0.0008995539 * cos(32*pi ((x^2 + y^2)^0.5)/15) +0.0009931555 * cos(33*pi ((x^2 + y^2)^0.5)/15) +0.0015552078 * cos(34*pi ((x^2 + y^2)^0.5)/15) -0.0003397407 * cos(35*pi ((x^2 + y^2)^0.5)/15) +0.0000663066 * cos(36*pi ((x^2 + y^2)^0.5)/15) -0.0002732666 * cos(37*pi ((x^2 + y^2)^0.5)/15) -0.0014145282 * cos(38*pi ((x^2 + y^2)^0.5)/15) +0.0000825822 * cos(39*pi ((x^2 + y^2)^0.5)/15) +0.0006140566 * cos(40*pi ((x^2 + y^2)^0.5)/15)"
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