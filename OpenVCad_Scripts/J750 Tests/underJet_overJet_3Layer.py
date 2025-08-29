import pyvcad as pv

root = pv.Union()
#Testing how grab cad print handles jetting air

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")  # Agilus
blue = materials.id("blue")  # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
yellow = materials.id("yellow") # air

#-- Geometry --
B = 18
H = 15
h1 = 0
h3 = 0.001

h2 = H - h1-h3

#-- Air Percentages --
a2 = [0.675,0.70,0.725]
print(a2)
a3 = [None] * len(a2)
for i in range(3):
    a3[i] = (H-h2)*a2[i] / h3
print("a3:" + str(a3))


for i in range(len(a3)):
    if a3[i] > 1.0:
        raise ValueError("Value #" +str(i+1)+ " of a3 is " +str(a3[i])+ " but must be less then 1.0")


for i in range(len(a3)):
    
    tempMesh = pv.Union()
    #Walls 
    wall_Mesh = pv.Mesh("MAC_LAB/STL Files/boxWCap.STL",blue)

    x_offset = 11
    y_offset = 17/2
    z_offset = 11

    wall_Mesh = pv.Translate(-x_offset,-y_offset,-z_offset,wall_Mesh)
    wall_Mesh = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),wall_Mesh)
    wall_Mesh = pv.Translate((i-1)* 2*B,0,y_offset,wall_Mesh)
    tempMesh.add_child(wall_Mesh)

    #Air Layer
    layer_1 = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(B,B,h1),yellow)
    layer_1 = pv.Translate((i-1)* 2*B,0,h1/2+2,layer_1)
    tempMesh.add_child(layer_1)

    #correctly jetted layer
    layer_2 = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(B,B,h2),yellow)
    layer_2_FG = pv.FGrade([str(a2[i]), str(1-a2[i])],[liquid_mat, yellow],True)
    print(a2[i])
    layer_2 = pv.Translate((i-1)* 2*B,0,h2/2+h1+2,layer_2)
    layer_2_FG.set_child(layer_2)
    tempMesh.add_child(layer_2_FG)

    #overJet Layer
    layer_3 = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(B,B,h3),yellow)
    layer_3 = pv.Translate((i-1)* 2*B,0,h1+h2+2+h3/2,layer_3)
    layer_3_FG = pv.FGrade([str(a3[i]), str(1-a3[i])],[liquid_mat, yellow],True)
    layer_3_FG.set_child(layer_3)
    
    tempMesh.add_child(layer_3_FG)

    #Cap
    cap = pv.RectPrism(pv.Vec3(0,0,2+H+1),pv.Vec3(B+4,B+4,2),blue)
    cap = pv.Translate((i-1)* 2*B,0,0,cap)
    tempMesh.add_child(cap)

    #Translating to Final Position and Adding to Root Node
    
    root.add_child(tempMesh)


tempRect = pv.RectPrism(pv.Vec3(0,11,0),pv.Vec3(50,8,35),red)
root = pv.Difference(root,tempRect)