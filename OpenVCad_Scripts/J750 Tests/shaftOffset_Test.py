import pyvcad as pv

#Material Deffinitions
materials = pv.default_materials()
red = materials.id("red")     #Agilus
blue = materials.id("blue")   #Vero
green = materials.id("green") #FullCure705

generateSupport = True
Support_offset = 1 #[mm]
STL_Location = "MAC_LAB/STL Files/ShafOffset_Test"

Vero_percent = 0.90
Agilus_percent = 1 - Vero_percent

#Import STL and Assign Gradient
testMesh = pv.Mesh(STL_Location + "/COAXIAL_SHAFTCONNECTOR-SPACING_TEST.STL", red)
testMesh = pv.Translate(-20/2,-85/2,0,testMesh)
testMesh = pv.Rotate(0,0,90,pv.Vec3(0,0,0),testMesh)

testFinal = pv.FGrade([str(Vero_percent),str(Agilus_percent)],[blue,red],True)
testFinal.set_child(testMesh)

#For generating our own supports without grid
if generateSupport == True:
    y = 20
    x = 85
    z = 26

    support = pv.Difference(
        pv.RectPrisim(pv.Vec3(0,0,z/2),pv.Vec3(x+2*Support_offset,y+2*Support_offset,z+2*Support_offset),green),
        testFinal)

    supportFinal = pv.FGrade([1],[green],True)


#Root time
root = pv.Union()
if generateSupport == True: root.add_child(supportFinal)
root.add_child(testFinal)