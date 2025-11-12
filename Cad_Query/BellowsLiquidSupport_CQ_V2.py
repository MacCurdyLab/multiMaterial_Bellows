#NOTES:
    
#======== Bellow Assembly ============
import cadquery as cq

#-------------------------------------
#       Variables
#-------------------------------------
pipe_ID = 3.5 #[mm] center diameter of bellows
internal_thick = 0.9 #[mm]

total_R = 12.5 #[mm] radius of entire bellow
total_H = 3.5 #[mm] entire height of bellows

edge_thick = 2.25 #[mm] thickness of outermost edge of bellows
edge_H = 0.75 # height of outtermost edge

baffle_D = 0.4

supportBoundary_thick = 0.2
veroBoundary_thick = 0.2
fillet_R = 0.26
fillet_R2 = 0.3

vero_thick = 0.1
 #[mm] thickness of vero keepout layer
support_thick = 0.2 #[mm] thickness of 705FullCure support keepout layer

#-------------------------------------
#       Outer Bellow
#-------------------------------------

#Sketch
#Start with Internal segments to be able to copy later
outerBellows_inside_sketch= (
    cq.Workplane()
    .lineTo(pipe_ID/2,0.0, forConstruction=True)
    .lineTo(pipe_ID/2,internal_thick+fillet_R)
    .lineTo(pipe_ID/2+edge_thick,internal_thick+fillet_R)
    .lineTo(total_R-fillet_R-edge_thick,total_H/2-fillet_R)
    .radiusArc((total_R -edge_thick,total_H/2),-fillet_R)
    )

#now create entire bellows sketch
outerBellows_sketch = cq.Workplane().add(outerBellows_inside_sketch.wires())
"""outerBellows_sketch = (outerBellows_sketch
                       .lineTo(total_R,total_H/2)
                       .lineTo(total_R,total_H/2-edge_H+fillet_R2)
                       .radiusArc((total_R-fillet_R2,total_H/2-edge_H),+fillet_R2)
                       .lineTo(total_R-edge_thick,total_H/2-edge_H)
                       .lineTo(pipe_ID/2+edge_thick+fillet_R,fillet_R)
                       .radiusArc((pipe_ID/2+edge_thick,0),fillet_R)
                       .lineTo(pipe_ID/2,0)
                       
                       )
"""

#just for debugging to show me where my selection is

"""
#Outter Line Segments of the bellows
outerBellows_sketch = (
    outerBellows_sketch
    .segment((total_R-edge_thick,total_H/2),(total_R,total_H/2))
    .segment((pipe_ID/2,0.0),(pipe_ID/2+edge_thick,0.0))
    .segment((pipe_ID/2+edge_thick,0.0),(pipe_ID/2+edge_thick,fillet_R))
    .segment((pipe_ID/2+edge_thick,fillet_R),(total_R-edge_thick,total_H/2-internal_thick) )
    .segment((total_R,total_H/2),(total_R,total_H/2-internal_thick))
    .segment((total_R,total_H/2-internal_thick),(total_R-edge_thick,total_H/2-internal_thick))
    .assemble()
    )

#Fillets:
outerBellows_sketch = (
    outerBellows_sketch
    .reset()
    .vertices(cq.NearestToPointSelector((pipe_ID/2+edge_thick,fillet_R)))
    .fillet(fillet_R)
    .reset()
    .vertices(cq.NearestToPointSelector((total_R,total_H/2-internal_thick)))
    .fillet(fillet_R2)
    .reset()
    .vertices(cq.NearestToPointSelector((total_R-edge_thick,total_H/2-fillet_R)))
    .fillet(fillet_R-.01)
    )





# Creating actuall bellows solid
bellowsBottom = (cq.Workplane()
                .placeSketch(outerBellows_sketch)
                .revolve(360)
                .translate((0,-total_H/2,0))
                )
bellowsTop = bellowsBottom.mirror("XZ")

bellows = bellowsBottom.union(bellowsTop)

#Export bellow to ".stl"
#cq.exporters.export(bellows, "bellows_1.stl")
"""

#-------------------------------------
#       Support-Housing Boundary
#-------------------------------------

# I think I might be able to to an offset feature from the internal line segment part of
# the bellows sketch, then translate that into position and revolve to get the support
supportHousing_sketch = (outerBellows_inside_sketch
                         .offset2D(vero_thick,'arc')
                         .edges("not (<Y or >X)")
                         )

#-------------------------------------
#       Fluid
#-------------------------------------

#Once I get the offset sketch for support-housing boundary I will do a 
# similar thing with the fluid