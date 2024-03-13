import cadquery as cq

# Create a new CadQuery workplane
workplane = cq.Workplane("XY")

# Create a box
box = workplane.box(10, 20, 30)
box.val().exportStep("box.step")

# Create a cylinder
cylinder = workplane.cylinder(radius=5, height=15)
cylinder.val().exportStep("cylinder.step")

# Create a sphere
sphere = workplane.sphere(radius=8)
sphere.val().exportStep("sphere.step")