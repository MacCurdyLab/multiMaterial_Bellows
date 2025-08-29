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
h1 = [1.0,2.0]
h2 = [None] * len(h1)

for i in range(len(h1)):
    h2[i] = H - h1[i]

#-- Air Percentages --
a2 = 0.70
print(h2)


for i in range(len(h2)):
    
    tempMesh = pv.Union()
    #Walls 
    wall_Mesh = pv.Mesh("MAC_LAB/STL Files/boxWCap.STL",blue)

    x_offset = 11
    y_offset = 17/2
    z_offset = 11

    wall_Mesh = pv.Translate(-x_offset,-y_offset,-z_offset,wall_Mesh)
    wall_Mesh = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),wall_Mesh)
    wall_Mesh = pv.Translate((i)* 2*B,0,y_offset,wall_Mesh)
    

    #Text
    textLabel = pv.Text(str(h1[i]),5,0.5,red)
    textLabel = pv.Translate((i)* 2*B,0,0.25,textLabel)
    wall_Mesh = pv.Difference(wall_Mesh,textLabel)

    tempMesh.add_child(wall_Mesh)
    tempMesh.add_child(textLabel)

    #Air Layer
    layer_1 = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(B,B,h1[i]),yellow)
    layer_1 = pv.Translate((i)* 2*B,0,h1[i]/2+2,layer_1)
    tempMesh.add_child(layer_1)

    #correctly jetted layer
    layer_2 = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(B,B,h2[i]),yellow)
    layer_2_FG = pv.FGrade([str(a2), str(1-a2)],[liquid_mat, yellow],True)
    
    layer_2 = pv.Translate((i)* 2*B,0,h2[i]/2+h1[i]+2,layer_2)
    layer_2_FG.set_child(layer_2)
    tempMesh.add_child(layer_2_FG)

    #Cap
    cap = pv.RectPrism(pv.Vec3(0,0,2+H+1),pv.Vec3(B+4,B+4,2),blue)
    cap = pv.Translate((i)* 2*B,0,0,cap)
    tempMesh.add_child(cap)

    #Adding to Root Node
    root.add_child(tempMesh)

#-- Section View --
#tempRect = pv.RectPrism(pv.Vec3(0,11,0),pv.Vec3(50,8,35),red)
#root = pv.Difference(root,tempRect)