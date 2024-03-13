import os
import FreeCAD
import Part
import Import

# Set the path to the directory containing the component files
component_dir = "/home/cad_files"

# Create a new document
doc = FreeCAD.newDocument()

# Iterate over the files in the component directory
for filename in os.listdir(component_dir):
    if filename.endswith(".step"):
        # Get the full path to the component file
        file_path = os.path.join(component_dir, filename)
        
        # Import the component file
        shape = Part.Shape()
        shape.read(file_path)
        obj = doc.addObject("Part::Feature", os.path.splitext(filename)[0])
        obj.Shape = shape
        
        # Set the label of the object to the filename without the .step suffix
        label = os.path.splitext(filename)[0]
        obj.Label = label

# Save the assembly file as .fcstd
assembly_path_fcstd = "assembly.fcstd"
doc.saveAs(assembly_path_fcstd)

# Export the assembly as .step
assembly_path_step = "assembly.step"
Import.export(doc.Objects, assembly_path_step)

# Close the document
FreeCAD.closeDocument(doc.Name)