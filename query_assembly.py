import FreeCAD
import Part
import os

# Load the assembly from a .fcstd file
assembly_path = "/home/assembly.fcstd"  # Replace with your file path
doc = FreeCAD.open(assembly_path)

# Find the part with the label 'box'
part_name = "sphere"  # Replace with the label of the part you're looking for
found_part = None
for obj in doc.Objects:
    if obj.Label == part_name:
        found_part = obj
        break

if found_part is not None:
    output_dir = "/home/"

    # Export this part as a new .step file in the created directory
    output_path = os.path.join(output_dir, f"{part_name}.step")
    Part.export([found_part], output_path)
    print(f"Exported {part_name} to {output_path}")
else:
    print(f"Part with label '{part_name}' not found in the assembly.")

# Close the document
FreeCAD.closeDocument(doc.Name)