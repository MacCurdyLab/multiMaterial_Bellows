# Sketch Tutorial
import cadquery as cq

# Defining Sketch
mySketch = (
    cq.Sketch()
    .trapezoid(4,3,90)
    .vertices()
    .circle(0.5,mode="s")
    .reset()
    .vertices()
    .fillet(0.25)
    .reset()
    .rarray(0.6,1,5,1)
    .slot(1.5,0.4,mode="s", angle=90)
    )

#Assigning sketch to a work plane and extruding
result = cq.Workplane("YZ").placeSketch(mySketch).extrude(1)