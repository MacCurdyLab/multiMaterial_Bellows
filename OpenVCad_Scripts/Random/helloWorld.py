import pyvcad as pv

# Load our material config. This provides a mapping between string name
# and IDs VCAD can use
materials = pv.MaterialDefs("configs/default.json")

# creating a 10[mm] cube centered at 0,0,0
center_point = pv.Vec3(0,0,0)
dimensions = pv.Vec3(10,10,10)

root = pv.RectPrism(center_point, dimensions, materials.id("red"))

