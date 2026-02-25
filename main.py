#-----------------------------------------------
#Main script for computational bellows rendering
#----------------------------------------------
#Initially writen by Andrew Heck (andrewlheck@yahoo.com) at MACLab at 

#to activate environment: .\MACPY\Scripts\activate

#Imports
import cadquery as cq
import scipy as sc
import numpy as np
from Cad_Query.bellow_stack import bellow_stack
import pyvcad as pv
import pyvcad_rendering as viz

#----------------------------
#------Bellows Settings------
#----------------------------
#File Information
STL_Location = "C:/Users/andre/Documents/SolidWorks/MACLAB/CAD_QUERYTESTS/" #Location to save STL files
shell_file = "shell.stl" #Name of shell STL file
fluid_file = "fluid.stl" #Name of fluid STL file
fluidWithHoles_file = "fluid_with_holes.stl" #Name of fluid with holes STL file
supportLayer_file = "supportLayer.stl" #Name of support layer STL file
veroKeepOut_file = "veroKeepOut.stl" #Name of vero keep-out STL file

gradientText = "bellow_materialGradient.txt" #Name of material gradient text file

#Render Settings
createBellowSTL = False #Whether to create new STL file of a half Bellow stack
createGradientFunction = False #Whether to create a .txt file containing bellow material gradient
showVCAD = True 

#Bellows Geometry Parameters
a = 2.25 #edge thickness [mm]
b = 0.75 #edge height [mm]
c = 1.75 #pipe radius [mm]
d = 5.06 #wall angle [deg]
e = 12.5 #total radius [mm]


supportLayer_thickness = 0.2 #thickness of the support layer between the fluid and shell        
capHeight = 2.0 #height of dome caps [mm]

#Bellows Material Parameters
fluidPercent = 0.725
numStacks = 3
includeBaffles = True
veroKeepOut = True #wether I want to include the vero keep out layer
bellowType = "single" #single or double bellows stack

#Multi Print Settings
num_bellowsToPrint = 1 #if single stack, how many stacks to print in one go
x_multiPrint = 60
y_multiPrint = 8

#----------------------------
#-----------Setup------------
#----------------------------
#creating initial STL of a half belllow stack using cadquery and creating material gradient for bellows
main_bellowStack = bellow_stack(
    a,b,c,d,e,
    (0,0,0),
    STL_Location,
    supportLayer_thickness,
    veroKeepOut,
    includeBaffles=True,
    saveSTL= createBellowSTL
)

f = main_bellowStack.f #half height of bellow stack [mm]

#Generate material gradient function
if createGradientFunction == True:
    print("0")

#read in material gradient from text file

vero_func = "0.5" #place holder for rn
agilus_func = "0.5"

#----------------------------------------------------
#---Rendering in VCAD--------------------------------
#----------------------------------------------------

#-- Material definitions --
materials = pv.default_materials
red = materials.id("red")            # Agilus
blue = materials.id("blue")          # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")        # Support
yellow = materials.id("yellow")      # Air

#-- placing stuff --
x_offset = 0
y_offset = 0
z_offset = 0

#-- Defining Root Node --
root = pv.Union()

#-----------------------------------------------------
#-- Importing meshes ---------------------------------
#-----------------------------------------------------

##-- Outter Bellow --
bellows1 = pv.Mesh(
    STL_Location + shell_file, red)
bellows1 = pv.Translate(-x_offset-e, -y_offset-e,0 , bellows1)

# === MATERIAL GRADING ===
# Gradient Type: gradient3
# Design Type: Single stack
# Stiff Section Settings: 70% Vero, 30% Agilus
# Soft  Section Settings: 15% Vero, 85% Agilus
# Gradient Start / End:   87.5% → 85%
# Gradient4 Vero/Agilus:  50% / 50%
#
# N (number of Fourier modes) = 60,  L = 15
#

# Use the computed Fourier‐series strings in the call below:
bellows_fgrade = pv.FGrade(
    [vero_func, agilus_func],
    [red, blue],
    True
)
bellows_fgrade.set_child(bellows1)

# Translate into position:
#hopefully can get rid of this if i can figure out how to set assembly location
bellows_fgrade = pv.Translate(x_offset+e, y_offset+e, 0, bellows_fgrade)

## -- Bottom Cap --
cap1fgrade = pv.FGrade(["0.95", "0.05"], [blue, red], True )
cap1fgrade.set_child(pv.Cylinder(pv.Vec3(0,-capHeight/2,0),capHeight,c+a,blue))

## -- Top Cap -- 
cap2fgrade = pv.Translate(0,(2*f*numStacks)+capHeight/2,0,cap1fgrade)

## -- Fluid-Solid Support Barrier --
supportBarrier1_mesh = pv.Mesh(STL_Location + supportLayer_file,green)

## -- Fluid-Solid Vero Barrier --
if veroKeepOut == True: #right now i dont see any reason to not include this ig
    supportBarrier2_mesh = pv.Mesh(
        STL_Location + veroKeepOut_file, blue
    )

## -- Baffles and Fluid --
fluidNoHoles1_mesh = pv.Mesh(
    STL_Location + fluid_file, liquid_mat
)
fluidAir_fgrade = pv.FGrade([str(fluidPercent),str(1-fluidPercent)],[liquid_mat,yellow],True)

if includeBaffles == True:
    fluidHoles1_mesh = pv.Mesh(
        STL_Location + fluidWithHoles_file, liquid_mat, True
    )

    baffles = pv.Difference(fluidNoHoles1_mesh, fluidHoles1_mesh)
    bafflesFgrade = pv.FGrade(['1'], [green], True) #defaults to first material defined so need to redefine mat
    bafflesFgrade.set_child(baffles)
    fluidAir_fgrade.set_child(fluidHoles1_mesh)
else:
    fluidAir_fgrade.set_child(fluidNoHoles1_mesh)

## -- Support Cap --
#should look into removing this guy lowkey
supportCap_H = 0.6; #[mm]
supportCap = pv.Cylinder(pv.Vec3(x_offset+e,y_offset+e,2+numStacks*f+supportCap_H/2+.527),3.5/2,supportCap_H,green)


#--------------------------------------------------------
#-- Repeating each Bellows Assmbly for N Bellows Stack --
#--------------------------------------------------------
repeatUnion = pv.Union()
repeatUnion.add_child(bellows_fgrade)         # Bellows Housing
#repeatUnion.add_child(supportBarrier1_mesh)   #705FullCure Support Layer
#repeatUnion.add_child(fluidAir_fgrade)        #Fluid
#repeatUnion.add_child(supportBarrier2_mesh)   #Vero Support Layer

if includeBaffles == True:
    #repeatUnion.add_child(bafflesFgrade)
    print("o")

# Union node for the entire stack of baffles excluding caps
fullStackUnion = pv.Union()
fullStackUnion.add_child(repeatUnion)

for i in range(numStacks-1):
    tempBellowsMesh = repeatUnion
    tempBellowsMesh = pv.Translate(0,0,f*2*(i+1),tempBellowsMesh)
    fullStackUnion.add_child(tempBellowsMesh)

fullStackUnion = pv.Difference(fullStackUnion,supportCap)

#--------------------------------------
#-- Union of all Meshes to Root Node --
#--------------------------------------
# Using a temporaty union before adding to root incase of multiprint
singleStack_Union = pv.Union()
singleStack_Union.add_child(fullStackUnion)
singleStack_Union.add_child(cap1fgrade)
singleStack_Union.add_child(cap2fgrade)
singleStack_Union.add_child(supportCap)

root.add_child(singleStack_Union)

#--------------------------------------
#-- Translation for MultiPrint --------
#--------------------------------------

#We want to do multiprint if num_bellowsToPrint > 1
if num_bellowsToPrint > 1:
    tempStack  = singleStack_Union
    for i in range(num_bellowsToPrint-1):
        tempStack = pv.Translate(x_multiPrint,y_multiPrint,0,tempStack)
        root.add_child(tempStack)

#--------------------------------------
#-- VCAD Rendering --------------------
#--------------------------------------
if showVCAD == True: viz.Render(root, materials)

viz.export(root,materials)