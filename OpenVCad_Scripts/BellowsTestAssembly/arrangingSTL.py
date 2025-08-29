import pyvcad as pv

# Materials
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  #agilus
blue = materials.id("blue") #vero
green = materials.id("green") #fluid

#Define Root
root = pv.Union()

temp = pv.Mesh(r"MAC_LAB/BellowsTestAssembly/leg_bellows/cap.STL",blue)
temp = pv.Translate(-4,-0.5,-4,temp)
temp = pv.Rotate(90,0,0,pv.Vec3(0,0,0),temp)
root.add_child(temp)