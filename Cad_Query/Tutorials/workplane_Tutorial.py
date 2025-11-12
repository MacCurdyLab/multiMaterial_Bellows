result = (
    cq.Workplane("front")
    .sketch()
    .lineTo(2.0, 0)
    .lineTo(2.0, 1.0)
    .threePointArc((1.0, 1.5), (0.0, 1.0))
    .close()
    .assemble()
    .vertices(">X")
    .fillet(.05)
    
)