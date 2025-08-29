import pyvcad as pv
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")            # Agilus

root = pv.Union()

stl_Location = "MAC_LAB/STL Files/DualWithBaffles"
bellows1 = pv.Mesh(
    stl_Location+"/Variable_AssemblyWithBaffles_usingIntersection - Variable Bellows 6 Stack-1 Variable_Bellow-6.STL", red)

root.add_child(bellows1)