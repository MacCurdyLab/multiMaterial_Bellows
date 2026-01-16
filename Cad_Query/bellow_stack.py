import cadquery as cq
import scipy as sc
import numpy as np

class bellow_stack:
    #-- Overarching Geometreis - -
    d_nom = 5.06 #[deg] wall angle for relaxed position
    f_nom = 1.75 #[mm] height of half bellow for relaxed position
    
    def __init__(self,a,b,c,d,e,loc,supportLayer_thic = 0.2, includeVeroKeepOut = True,includeLiquid = True, saveSTL = False):
        #------------------------------
        # Creates a Stack of Bellows
        # a - edge thickness
        # b - edge height
        # d - wall angle
        # e - total radius
        # f - half height of bellow stack
        # n - number of bellows in a stack
        # loc = [x,y,z] - position of the center of the bottom bellow
        self.A_tot = (self.f_nom-b)*(a+c+(self.f_nom-b)*np.tan(np.pi*(90-self.d_nom)/180))
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = sc.optimize.fsolve(self.__Atot_func,1)
        self.loc = loc
        
        self.supportLayer_offset = supportLayer_thic
        
        #-----------------------------------
        #Create A Single Bellows Layer
        #-----------------------------------
        #Render individual parts
        fluid_object = self.__render_fluid()
        supportLayer_object = self.__render_supportLayer()
        shell_object = self.__render_outerbellows(includeVeroKeepOut)
        if includeVeroKeepOut == True:
            veroKeepOut_object = self.__render_veroKeepOut()
        
        #Assemble into single Assembly
        self.TopLevelAssembly = (
            cq.Assembly()
            .add(fluid_object)
            .add(supportLayer_object)
            .add(shell_object)
            )
        if includeVeroKeepOut == True: self.TopLevelAssembly.add(veroKeepOut_object)
        
        #Finalize and return assembly
        #self.TopLevelAssembly.solve() #uncomment once I add constraints
        show_object(self.TopLevelAssembly)
    
    
    #-------------------------------------------------
    #implicit function of the internal cross-sectional
    #area of the bellows. Used in __init__()
    #-------------------------------------------------
    def __Atot_func(self,f):
        return (f-self.b)*(self.a+self.c+(f-self.b) * np.tan((90-self.d)*np.pi/180))-self.A_tot
    
    #-------------------------------------------------
    # Creates the Sketch for Everything
    #-------------------------------------------------
    def __bellows_sketch(self,sketchType,includeVeroKeepOut = False):
        fillet_R = 0.26 #[mm]
        
        #Depends on What type of bellows
        if includeVeroKeepOut == True:
            vero_offset = 0.2 #[mm]
            if sketchType == "veroKeepOut":
                crossSection_sketch = (
                    cq.Workplane("front")
                    .lineTo(self.c,0.0,forConstruction=True)
                    .lineTo(self.c,self.b)
                    .lineTo(self.c+self.a,self.b)
                    .lineTo(self.e-self.a+fillet_R,self.f-fillet_R)
                    .radiusArc((self.e-self.a+2*fillet_R,self.f),-fillet_R) #end of inside
                    .lineTo(self.e-self.a+2*fillet_R+vero_offset,self.f)
                    .radiusArc((self.e-self.a+fillet_R,self.f-fillet_R-vero_offset),(fillet_R+vero_offset))
                    .lineTo(self.a+self.c,self.b-vero_offset)
                    .lineTo(self.c+vero_offset,self.b-vero_offset)
                    .lineTo(self.c+vero_offset,0.0)
                    .close()
                    )
            elif sketchType == "shell":
                crossSection_sketch = (
                    cq.Workplane("front")
                    .lineTo(self.c+vero_offset,0.0,forConstruction=True)
                    .lineTo(self.c+self.a,0.0)
                    .radiusArc((self.c+self.a+fillet_R,fillet_R),fillet_R)
                    .lineTo(self.e-self.a,self.f-self.b)
                    .lineTo(self.e,self.f-self.b)
                    .lineTo(self.e,self.f) #end of outside
                    .lineTo(self.e-self.a+2*fillet_R+vero_offset,self.f)
                    .radiusArc((self.e-self.a+fillet_R,self.f-fillet_R-vero_offset),(fillet_R+vero_offset))
                    .lineTo(self.a+self.c,self.b-vero_offset)
                    .lineTo(self.c+vero_offset,self.b-vero_offset)
                    .lineTo(self.c+vero_offset,0.0)
                    .close()
                    )
            else:
                raise ValueError("Only shell and veroKeepOut objects can be rendered when includeVeroKeepOut is true.")
        
        else: #for when we aren't dealing with vero keepout layer
            if sketchType == "shell":
                crossSection_sketch = (
                    cq.Workplane("front")
                    .lineTo(self.c,0.0,forConstruction=True)
                    .lineTo(self.c,self.b)
                    .lineTo(self.c+self.a,self.b)
                    .lineTo(self.e-self.a+fillet_R,self.f-fillet_R)
                    .radiusArc((self.e-self.a+2*fillet_R,self.f),-fillet_R)#end point rn
                    .lineTo(self.e,self.f)
                    .lineTo(self.e,self.f-self.b)
                    .lineTo(self.e-self.a,self.f-self.b)
                    .lineTo(self.c+self.a+fillet_R,fillet_R)
                    .radiusArc((self.c+self.a,0.0),-fillet_R)
                    .lineTo(self.c,0.0)
                    .close()
                    )
            
            elif sketchType == "fluid":
                crossSection_sketch = (
                    cq.Workplane("front")
                    .lineTo(0.0,self.f)
                    .lineTo(self.e-self.a+2*fillet_R-self.supportLayer_offset,self.f)
                    .lineTo(self.c+self.a,self.b+self.supportLayer_offset)
                    .lineTo(self.c-self.supportLayer_offset,self.b+self.supportLayer_offset)
                    .lineTo(self.c-self.supportLayer_offset,0.0)
                    .close()
                    )
            
            elif sketchType == "supportLayer":
                crossSection_sketch = (
                    cq.Workplane("front")
                    .lineTo(self.c,0.0,forConstruction=True)
                    .lineTo(self.c,self.b)
                    .lineTo(self.c+self.a,self.b)
                    .lineTo(self.e-self.a+fillet_R,self.f-fillet_R)
                    .radiusArc((self.e-self.a+2*fillet_R,self.f),-fillet_R) #end of inside
                    .lineTo(self.e-self.a+2*fillet_R-self.supportLayer_offset,self.f)
                    .lineTo(self.c+self.a,self.b+self.supportLayer_offset)
                    .lineTo(self.c-self.supportLayer_offset,self.b+self.supportLayer_offset)
                    .lineTo(self.c-self.supportLayer_offset,0.0)
                    .close()
                    )
            else:
                raise ValueError("SKETCH TYPE DOES NOT EXSIST")
        
        show_object(crossSection_sketch)
        return(crossSection_sketch)
    
    #-------------------------------------------------
    #Creates the outer bellow shell
    #-------------------------------------------------
    def __render_outerbellows(self,includeVeroKeepOut=False):
        #call sketch function
        shell = self.__bellows_sketch("shell",includeVeroKeepOut)
        shell = shell.revolve(360).translate((0,-self.f,0))
        show_object(shell,options={"color": (240,249,232)})
        shell.faces("<Y").tag("mate1")
        return(shell)

    #-------------------------------------------------
    #Create Model for Fluid Inside of bellows
    #-------------------------------------------------
    def __render_fluid(self):
        fluid = self.__bellows_sketch("fluid")
        fluid = fluid.revolve(360).translate((0,-self.f,0))
        show_object(fluid,options={"color": (186,228,188)})
        fluid.faces("<Y").tag("mate1")
        return(fluid)
    
    #-------------------------------------------------
    #Create Model for Support Between Liquid and Solid
    #-------------------------------------------------
    def __render_supportLayer(self):
        supportLayer = self.__bellows_sketch("supportLayer")
        supportLayer = supportLayer.revolve(360).translate((0,-self.f,0))
        show_object(supportLayer,options={"color": (123,204,196)})
        supportLayer.faces("<Y").tag("mate1")
        return(supportLayer)
    
    def __render_veroKeepOut(self):
        veroKeepOut = self.__bellows_sketch("veroKeepOut",True)
        veroKeepOut = veroKeepOut.revolve(360).translate((0,-self.f,0))
        show_object(veroKeepOut,options={"color": (67,162,202)})
        veroKeepOut.faces("<Y").tag("mate1")
        return(veroKeepOut)
    
    #-------------------------------------------------
    #Connects A Bellow to a List of other Bellows via
    #piping.
    #-------------------------------------------------
    def connect_Bellows(self,pipe_ID,pipe_OD,bellows_to_connect):
        return("0")

directory = ""
angle = 5.06

mybellow = bellow_stack(2.25,1.05,1.75,angle,12.5,(0,0,0))
print(mybellow.f)

#Export assembly as .step files
mybellow.TopLevelAssembly.export("bellowHalfAssembly.stl")