id = 22.35
od = id + 8

h = 7
bolt_od = 8
bolt_id = 4
arm_w = 8
arm_l = 60  # from center
hole_pos = ((17.5,0), (-17.5,0))

s = ( cq.Sketch()
    .circle(od/2)
    .circle(id/2, mode='s')
    .push(hole_pos)
    .circle(bolt_od/2)
    .circle(bolt_id/2, mode='s')
    .clean()
    .reset()
    .vertices('>Y or <Y')
    .fillet(1)
)


result = cq.Workplane().placeSketch(s).extrude(h).faces('|Z').chamfer(0.5)
show_object(s)
show_object(result)