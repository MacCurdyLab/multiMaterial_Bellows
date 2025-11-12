import cadquery as cq

# Variables
height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0
 #M2 Socket screw

# Base
result = (
    cq.Workplane("XY")
    .box(height,width,thickness)
    .faces(">Z")
    .workplane()
    .hole(diameter)
    .faces(">Z")
    .rect(height-padding,width-padding,forConstruction=2)
    .vertices()
    .cboreHole(2.4,4.4,2.1)
    .edges("|Z")
    .fillet(2.0)
)

# Render the solid
show_object(result)

# Export
cq.exporters.export(result, "result.stl")