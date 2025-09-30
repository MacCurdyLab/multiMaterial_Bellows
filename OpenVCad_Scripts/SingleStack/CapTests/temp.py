import pyvcad as pv
materials = pv.default_materials()
red = materials.id("red")
blue = materials.id("blue")

root = pv.Union()
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/Sloped_Cap_wALLtHICKNESS0-8"
cap2_mesh = pv.Mesh(STL_Location+"/slopedStart_domeCap.STL",red)
cap2_mesh = pv.Translate(-20.186845/2-.1562775,-5.2/2,-20.5/2,cap2_mesh)
cap2_mesh = pv.Rotate(-90,0,0,pv.Vec3(0,0,0),cap2_mesh)
cap2_mesh = pv.Translate(0,0,2.600002,cap2_mesh)

root.add_child(cap2_mesh)