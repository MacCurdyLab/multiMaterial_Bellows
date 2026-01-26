import pyvcad as pv
import pyvcad_rendering as viz

# Load our material config. This provides a mapping between string names 
# and IDs VCAD can use
materials = pv.default_materials
red = materials.id("red")            # Agilus
shell_file = "shell.stl" #Name of shell STL file
root = pv.Union()
STL_Location = "C:/Users/andre/Documents/SolidWorks/MACLAB/CAD_QUERYTESTS/" #Location to save STL files
root.add_child(pv.Mesh(STL_Location + shell_file, red)) 


viz.Render(root, materials) # Render the cube via a pop-up window