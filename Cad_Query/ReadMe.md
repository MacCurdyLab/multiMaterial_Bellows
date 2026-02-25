
# Cad Query Testing

#### Cad Query is a script based CAD platform. It is not currently fully integrated with OpenVCAD, but by saving CadQuery models as .STL or .STEP files and then importing them into OpenVCAD using the mesh() function you can generate a CAD model and asign material gradients in a single Python script.

## Most Up to Date Code:

After installing all libraries you should be able to run [main.py](main.py) and fully generate a single stack of bellows. This script calls [bellow_stack.py](bellow_stack.py) which creates and exports the bellows stack CAD model. It can also be run independently.

As of 2/24/2026 I have not actually tried exporting png stacks generated using these scripts.

*add picture of dimensioned bellows*

## Other Code:
Code in the *Trials* and *Tutorials* directories were mostly tests while I was learning how to use CadQuery library. CadQuery has really good tutorials that can be found [here](https://cadquery.readthedocs.io/en/latest/examples.html).

## Known Issues:

- Cad Query and OpenVCAD use different versions of [VTK](https://vtk.org/). Code still renders but bellows don't display properly. Not certain if this is because of this or not.