import bpy
import os
import sys

input_model = sys.argv[-2] # one to the end is model name
export_png = sys.argv[-1] # last one is the png

assert(input_model.lower().endswith("stl"))
assert(export_png.lower().endswith("png"))

# assert(len(argv)==1)
# model = '/home/mmf159/Downloads/easter-egg-challenge-1.stl';

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
bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
scene.cursor_location = (0, 0, 0)
bpy.ops.object.origin_set(type="ORIGIN_CURSOR")

bpy.context.scene.render.filepath = export_png
bpy.ops.render.render(write_still=True)
