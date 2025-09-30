import pyvcad as pv

root = pv.Union()
#Testing how grab cad print handles jetting air
fluidPercent = 0.75

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  # Agilus
blue = materials.id("blue")  # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
yellow = materials.id("yellow") # air
void = materials.id("void")

fileLocation = "MAC_LAB/STL Files/BoxTest3"

#Walls 
wall_Mesh = pv.Mesh(fileLocation+"/testBox_ASSEMBLY - fluidTestBox_Hollow-1.STL",blue)
fluid_mesh = pv.Mesh(fileLocation+"/testBox_ASSEMBLY - innerFluid_fluidTestBox-1.STL",liquid_mat)
fluidGrad = pv.FGrade([str(fluidPercent),str(1-fluidPercent)],[liquid_mat,yellow],True)
fluidGrad.set_child(fluid_mesh)

wall_Mesh = pv.Difference(wall_Mesh,fluid_mesh)

root.add_child(wall_Mesh)
root.add_child(fluidGrad)

#Section View
#tempRect = pv.RectPrism(pv.Vec3(11,0,11),pv.Vec3(22,8,22),red)
#root = pv.Difference(root,tempRect)