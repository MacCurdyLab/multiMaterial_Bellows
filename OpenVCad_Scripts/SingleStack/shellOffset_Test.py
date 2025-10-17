# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/Sloped_Cap_wALLtHICKNESS0-8"

#-- Material definitions --
materials = pv.default_materials()
red = materials.id("red")            # Agilus
blue = materials.id("blue")          # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")        # Support
yellow = materials.id("yellow")      # Air

#-- Dimensions of part --
mainHeight = 3.5   # Dr. Mac's: 3.5[mm]
mainD = 25         # Dr. Mac's: 25[mm]
BottomcapHeight = 2      #[mm]
topCapHeight = 1.2 #[mm]

#-- Stack Settings --
fluidPercent = 0.725
numStacks = 3
includeBaffles = True
num_bellowsToPrint = 4

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
bellows = pv.Mesh(
    STL_Location + "/variableNumberBellowsStack_ASSEMBLY - Variable_Bellow-1.STL", red)
bellows = pv.Translate(-x-mainD/2, -y-mainD/2,0 , bellows)

bellows = pv.Translate(x+mainD/2, y+mainD/2, 0, bellows)

#-- Vero Offset Layer --
tempFGrade = pv.FGrade(['1'],[blue],True)
vero_offset_layer = pv.Offset(-0.1,bellows)
tempFGrade.set_child(vero_offset_layer)
vero_offset_layer = tempFGrade

#-- FullCure705 Offset Layer --

#------------------------------------------------------
#-- Root Union ----------------------------------------
#------------------------------------------------------

#root.add_child(bellows)
root.add_child(vero_offset_layer)
root.add_child(bellows)


#-- Section View --
#Bottom
#tempRect = pv.RectPrism(pv.Vec3(x+mainD/2,y+mainD/2,0),pv.Vec3(mainD,mainD,8),red)
#Side
tempRect = pv.RectPrism(pv.Vec3(x,y,(numStacks*mainHeight)/2+topCapHeight),pv.Vec3(50,25,20),red)
root = pv.Difference(root,tempRect)