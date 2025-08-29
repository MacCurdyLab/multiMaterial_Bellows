import pyvcad as pv



myText = pv.Text("1.0", 5.0,1.0,1,pv.FontAspect.Regular,"Consolas",pv.HorizontalAlignment.Center,pv.VerticalAlignment.Center)
myText = pv.Translate(0,2.448730,0,myText)
myText = pv.Rotate(90,0,0,pv.Vec3(0,0,0),myText)
myText = pv.Translate(0,0,5,myText)
root = pv.Union()
root.add_child(myText)