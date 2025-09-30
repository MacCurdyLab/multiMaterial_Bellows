import pyvcad as pv

#----------------------
#------- SETUP --------
#----------------------

#-- STL File Directory --
STL_Location = "MAC_LAB/STL Files/VariableSingleStack/spaceForSupportCap_wALLtHICKNESS0-8"

#-- Material definitions --
materials = pv.MaterialDefs("configs/default.json")
red = materials.id("red")            # Agilus
blue = materials.id("blue")          # Vero
liquid_mat = materials.id("liquid")  # Liquid matieral
green = materials.id("green")        # Support
yellow = materials.id("yellow")      # Air

#-- Dimensions of part --
Lx = 18       #[mm]
Ly = Lx       #[mm]
Lz = Lx       #[mm]
t_walls = 3.5 #[mm]
t_supp = 0.2  #[mm]

#Baffle Settings
D_baff = 0.5  #[mm] diameter of baffles
N_baff = 15   #number of baffles per row
baff_spacing = (Lx-t_supp*2) / (N_baff+1)
baff_center = pv.Vec3(t_walls+t_supp+baff_spacing,t_walls+t_supp+baff_spacing,0)

#-- Stack Settings --
fluidPercent = 0.725
includeBaffles = True

#-----------------------
#-- Defining Geometry --
#-----------------------
#Main Housing
housing = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(Lx+2*t_walls,Ly+2*t_walls,Lz+2*t_walls),blue)
housing = pv.Shell(-t_walls,housing)

#Outter Support
support_fluidHousing = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(Lx,Ly,Lz),green)
support_fluidHousing = pv.Shell(-t_supp,support_fluidHousing)

#Baffles
if includeBaffles:
    baffle_single = pv.Cylinder(baff_center, D_baff/2, Lz-2*t_supp, green)
    baffle_union = pv.Union()
    
    for i in range(N_baff):
        for j in range(N_baff):
            baffle_temp = baffle_single
            baffle_temp = pv.Translate(-i*baff_spacing,-j*baff_spacing,0,baffle_temp)
            baffle_union.add_child(baffle_temp)

#Fluid
fluid = pv.RectPrism(pv.Vec3(0,0,0),pv.Vec3(Lx-2*t_supp,Ly-2*t_supp,Lz-2*t_supp),liquid_mat)

if includeBaffles:
    fluid = pv.Difference(fluid,baffle_union)



#---------------
# ROOT
#---------------
root = pv.Union()
root.add_child(housing)
root.add_child(support_fluidHousing)
root.add_child(fluid)
if includeBaffles: 
    root.add_child(baffle_union)

tempRect = pv.RectPrism(pv.Vec3(0,0,12.5),pv.Vec3(10,Ly+2*t_walls,Lz+2*t_walls),red)
#tempRect = pv.RectPrism(pv.Vec3(12.5,0,0),pv.Vec3(10,Ly+2*t_walls,Lz+2*t_walls),red)
root = pv.Difference(root,tempRect)
