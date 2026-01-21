#----------------------------
#Main script for computational bellows rendering
#----------------------------

#to activate environment: .\multiMaterial_Bellows\Scripts\activate

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
#File Locations
stlSaveLocation = "./" #Location to save STL files

#Render Settings'
createBellowSTL = True #Whether to create new STL file of a half Bellow stack
createGradientFunction = False #Whether to create a .txt file containing bellow material gradient


#Bellows Geometry Parameters


#Bellows Material Parameters


#----------------------------
#-----------Setup------------
#----------------------------
#creating initial STL of a half belllow stack using cadquery and creating material gradient for bellows
if createBellowSTL == True:
    #Create Bellows Object
    my_bellow_stack = bellow_stack(
        a = 0.4, #edge thickness [mm]
        b = 0.5, #edge height [mm]
        c = 0.4, #edge thickness [mm]
        d = 5.06, #wall angle [deg]
        e = 6.0, #total radius [mm]
        loc = [0,0,0], #location of bottom center of bellows stack [x,y,z] in mm
        supportLayer_thic = 0.2, #thickness of support layer [mm]
        includeVeroKeepOut = True, #whether to include vero keep-out volume
        includeLiquid = True, #whether to include fluid volume
        saveSTL = createBellowSTL #whether to save STL file
    )

#NOTE: by rob meeting have this main script roughed out, and make an excel sheet of future print plans to keep stuff organized