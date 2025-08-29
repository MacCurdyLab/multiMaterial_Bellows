import pyvcad as pv

materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")
blue = materials.id("blue")

myPrisim = pv.RectPrism(pv.Vec3(0,0,0),(2,4,2),red)

root = myPrisim