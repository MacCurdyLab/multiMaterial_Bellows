import pyvcad as pv

root = pv.Union()
#Testing how grab cad print handles jetting air

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  # Agilus
blue = materials.id("blue")  # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
yellow = materials.id("yellow") # air
void = materials.id("void")



#Walls 
wall_Mesh = pv.Mesh("MAC_LAB/STL Files/BoxTest2/Assem1 - box-1.STL",blue)
bottomBox_Mesh = pv.Mesh("MAC_LAB/STL Files/BoxTest2/Assem1 - fluidBox-1.STL",yellow)
topBox_Mesh = pv.Mesh("MAC_LAB/STL Files/BoxTest2/Assem1 - fluidBox-2.STL",liquid_mat)

root.add_child(wall_Mesh)
root.add_child(bottomBox_Mesh)
root.add_child(topBox_Mesh)

x = 0.14543 -.000998
y = 0.174116
z = 2.640403

root = pv.Translate(-x-36/2,-y-28/2,-z-12,root)
root = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),root)

#tempRect = pv.RectPrism(pv.Vec3(0,-12,0),pv.Vec3(36,8,28),red)
#root = pv.Difference(root,tempRect)
#root = pv.Translate(0,0,1,root)