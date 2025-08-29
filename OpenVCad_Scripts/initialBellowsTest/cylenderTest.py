import pyvcad as pv

materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")
blue = materials.id("blue")

#Dimensions of part
mainHeight = 8 #DR Mac's: 3.5mm
mainD = 2*22.6054 #DR MAC's: 25mm

fgrade = pv.FGrade(["r/22.6054*100","100-r/22.6054*100"],
                   [red, blue], True)
fgrade.set_child(
    #pv.Mesh("MAC_LAB/initialBellowsTest/steerable_bellows_solid.STL", red)
    #pv.Mesh("MAC_LAB/initialBellowsTest/bellows_v1_heckAndrew.STL", red)
    pv.Cylinder(pv.Vec3(0,0,0),mainD/2,mainHeight)
)

#fgrade = pv.Translate(-mainD/2, -mainHeight/2, -mainD/2, fgrade)
#fgrade = pv.Rotate(90,0,0, pv.Vec3(0,0,0), fgrade)

root = fgrade