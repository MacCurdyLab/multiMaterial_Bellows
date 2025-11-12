# ── SinglStack.py ────────────────────────────────────────────────────────────────
import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableDualStack/UpdatedSTLs"

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
topCapHeight = 1.2       #[mm]
stackOffset = 37         #[mm] distance between bellows stacks centeral axes

#-- Stack Settings --
fluidPercent = 0.725
numStacks = 6
includeBaffles = True
num_bellowsToPrint = 1

#-- Housing Settings --
housingVeroPercent = 1

#-- placing stuff --
x = 0.125
y = 0.125
z = 0.727

#-- Defining Root Node --
root = pv.Union()

#-----------------------------------------------------
#-- Importing meshes ---------------------------------
#-----------------------------------------------------
#-- Housing Assembly --
housingAssembly = pv.Mesh(
    STL_Location + "/DoubleStack_Assembly - HousingAssemblyDual-1.STL",red,True
)
housingAssembly_FGrade = pv.FGrade([str(housingVeroPercent),str(1-housingVeroPercent)], [blue,red], True)
housingAssembly_FGrade.set_child(housingAssembly)

#-- Housing Fluid --
housingFluid_noHoles = pv.Mesh(
    STL_Location + "/DoubleStack_Assembly - HousingLiquidWBHoles-1.STL", liquid_mat,True
)
housingFluid_FGrade = pv.FGrade([str(fluidPercent),str(1-fluidPercent)],[liquid_mat,yellow],True)

if includeBaffles == True:
    housingFluid_Holes = pv.Mesh(
    STL_Location + "/DoubleStack_Assembly - HousingLiquidWBHoles-2.STL", liquid_mat,True
    )
    assemblyBaffles = pv.Difference(housingFluid_noHoles,housingFluid_Holes)
    assemblyBaffles_FGrade = pv.FGrade(['1'], [green], True)
    assemblyBaffles_FGrade.set_child(assemblyBaffles)
    housingFluid_FGrade.set_child(housingFluid_Holes)
else:
    housingFluid_FGrade.set_child(housingFluid_noHoles)


#-- Outter Bellow --
bellows1 = pv.Mesh(
    STL_Location + "/DoubleStack_Assembly - Variable_Bellow-1.STL", red)
bellows1 = pv.Translate(-x-mainD/2, -y-mainD/2,0 , bellows1)

bellows_fGrade = pv.FGrade(
    [str(housingVeroPercent),str(1-housingVeroPercent)], [blue,red], True
)

bellows_fGrade.set_child(bellows1)

# Translate into position:
bellows_fGrade = pv.Translate(x+mainD/2, y+mainD/2, 0, bellows_fGrade)

# -- Fluid-Solid Support Barrier --
supportBarrier1_mesh = pv.Mesh(
    STL_Location + "/DoubleStack_Assembly - Variable_Support-1.STL",green
)

# -- Baffles and Fluid --
fluidNoHoles1_mesh = pv.Mesh(
    STL_Location + "/DoubleStack_Assembly - Variable_Fluid-2.STL", liquid_mat
)
fluidAir_fGrade = pv.FGrade([str(fluidPercent),str(1-fluidPercent)],[liquid_mat,yellow],True)

if includeBaffles == True:
    fluidHoles1_mesh = pv.Mesh(
        STL_Location + "/DoubleStack_Assembly - Variable_Fluid-1.STL", liquid_mat
    )
    baffles = pv.Difference(fluidNoHoles1_mesh, fluidHoles1_mesh)
    bafflesFGrade = pv.FGrade(['1'], [green], True)
    bafflesFGrade.set_child(baffles)
    fluidAir_fGrade.set_child(fluidHoles1_mesh)
else:
    fluidAir_fGrade.set_child(fluidNoHoles1_mesh)


#--------------------------------------------------------
#-- Repeating each Bellows Assmbly for N Bellows Stack --
#--------------------------------------------------------
repeatUnion = pv.Union()
repeatUnion.add_child(bellows_fGrade)         # Bellows Housing
repeatUnion.add_child(supportBarrier1_mesh)   #705FullCure Support Layer
repeatUnion.add_child(fluidAir_fGrade)        #Fluid


if includeBaffles == True:
    repeatUnion.add_child(bafflesFGrade)

# Union node for the entire stack of baffles excluding caps
fullStackUnion = pv.Union()
fullStackUnion.add_child(repeatUnion)

for i in range(numStacks-1):
    tempBellowsMesh = repeatUnion
    tempBellowsMesh = pv.Translate(0,0,mainHeight*(i+1),tempBellowsMesh)
    fullStackUnion.add_child(tempBellowsMesh)

# Copying Stack To other Side

fullStackUnion_2 = pv.Translate(0,stackOffset,0,fullStackUnion)

#--------------------------------------
#-- Union of all Meshes to Root Node --
#--------------------------------------
# Using a temporaty union before adding to root incase of multiprint
dualStack_Union = pv.Union()
dualStack_Union.add_child(fullStackUnion)
dualStack_Union.add_child(fullStackUnion_2)
dualStack_Union.add_child(housingFluid_FGrade)
dualStack_Union.add_child(housingAssembly_FGrade)

if includeBaffles == True:
    dualStack_Union.add_child(assemblyBaffles_FGrade)

root.add_child(dualStack_Union)

#---------------------------
#-- Translation for MultiPrint
#--------------------------------

#We want to do multiprint if num_bellowsToPrint > 1
if num_bellowsToPrint > 1:
    tempStack  = dualStack_Union
    for i in range(num_bellowsToPrint-1):
        tempStack = pv.Translate(60,8,0,tempStack)
        root.add_child(tempStack)

#-- Section View --
#Bottom
#tempRect = pv.RectPrism(pv.Vec3(x+mainD/2,y+mainD/2,0),pv.Vec3(mainD,mainD,8),red)
#Side
#tempRect = pv.RectPrism(pv.Vec3(x,y,(numStacks*mainHeight)/2+topCapHeight),pv.Vec3(50,120,40),red)

#root = pv.Difference(root,tempRect)