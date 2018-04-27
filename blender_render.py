import bpy
import os
import sys
import math

input_model = sys.argv[-2] # one to the end is model name
export_png = sys.argv[-1] # last one is the png

assert(input_model.lower().endswith("stl"))
assert(export_png.lower().endswith("png"))

scene = bpy.context.scene
bpy.ops.import_mesh.stl(filepath=input_model)

imported = bpy.context.selected_objects[0]
imported_obj = bpy.data.objects[imported.name]
dim = imported_obj.dimensions
max_dim = max(max(dim.x, dim.y), dim.z) # only look at dimx dimy
scale_factor = 6/max_dim;

bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
dim = imported_obj.dimensions

# https://blender.stackexchange.com/questions/24015/how-to-place-objects-on-the-center-of-the-ground-plane-via-python
bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN", center="BOUNDS")
imported_obj.location = (0, 0, 0)

filename, file_extension = os.path.splitext(export_png)

rotation_eulers = [
    (0, 0, 0),
    (0, 0, math.pi/2),
    (0, 0, 2*math.pi/2),
    (0, 0, 3*math.pi/2),
    (0, 0, 4*math.pi/2),
    (math.pi/2, 0, 0),
    (-math.pi/2, 0, 0),
]

counter = 0
for obj in bpy.data.objects: # used for multiple cameras
    if obj.type == "CAMERA":
        bpy.data.scenes[0].camera = obj

        # 6 rotation
        #  for rotation_euler in rotation_eulers:
            #  bpy.context.scene.render.filepath = filename+str(counter)+file_extension
            #  imported_obj.rotation_euler = rotation_euler
            #  bpy.ops.render.render(write_still=True)
            #  counter += 1

        # no rotation
        bpy.context.scene.render.filepath = filename+str(counter)+file_extension
        bpy.ops.render.render(write_still=True)
