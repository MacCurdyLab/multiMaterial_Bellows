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
veroBoundary_thick = 0.1
fillet_R = 0.16

#-------------------------------------
#       Outer Bellow
#-------------------------------------

#Sketch
outerBellows_sketch= (
    cq.Sketch()
    .segment((0.0,0.0),(pipe_ID/2,0.0), forConstruction=True)
    .segment((pipe_ID/2,0.0),(pipe_ID/2,internal_thick+fillet_R))
    .segment((pipe_ID/2,internal_thick+fillet_R),(pipe_ID/2+edge_thick,internal_thick+fillet_R))
    .segment((pipe_ID/2+edge_thick,internal_thick+fillet_R),(total_R-fillet_R-edge_thick,total_H/2-fillet_R))
    .segment((total_R-fillet_R-edge_thick,total_H/2-fillet_R),(total_R-edge_thick,total_H/2-fillet_R))
    .segment((total_R-edge_thick,total_H/2-fillet_R),(total_R-edge_thick,total_H/2))
    .segment((total_R-edge_thick,total_H/2),(total_R,total_H/2))
    .segment((pipe_ID/2,0.0),(pipe_ID/2+edge_thick,0.0))
    .segment((pipe_ID/2+edge_thick,0.0),(pipe_ID/2+edge_thick,fillet_R))
    .segment((pipe_ID/2+edge_thick,fillet_R),(total_R-edge_thick,total_H/2-internal_thick) )
    .segment((total_R,total_H/2),(total_R,total_H/2-internal_thick))
    .segment((total_R,total_H/2-internal_thick),(total_R-edge_thick,total_H/2-internal_thick))
    .assemble(tag="face")
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