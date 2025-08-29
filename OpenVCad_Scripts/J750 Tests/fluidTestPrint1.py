import pyvcad as pv

root = pv.Union()
#Testing if the printer is over or under jetting fluid 

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  # Agilus
blue = materials.id("blue")  # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")

#Walls 
wall_Mesh = pv.Mesh("MAC_LAB/STL Files/BoxTest1/Assem1 - box-1.STL",blue)
fluidBox_Mesh = pv.Mesh("MAC_LAB/STL Files/BoxTest1/Assem1 - fluidBox-1.STL",liquid_mat)

root.add_child(wall_Mesh)
root.add_child(fluidBox_Mesh)

root = pv.Translate(-0.094430-26/2,-13/2-0.174116,-1.640402-26/2,root)
root = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),root)
root = pv.Translate(0,0,6.5,root)