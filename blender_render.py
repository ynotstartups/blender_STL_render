import bpy
import os
import sys

print(sys.argv)

input_model = sys.argv[-2] # one to the end is model name
export_png = sys.argv[-1] # last one is the png

print(input_model, "tiger", export_png, "tiger")

assert(input_model.lower().endswith("stl"))
assert(export_png.lower().endswith("png"))

# assert(len(argv)==1)
# model = '/home/mmf159/Downloads/easter-egg-challenge-1.stl';

scene = bpy.context.scene
bpy.ops.import_mesh.stl(filepath=input_model)

imported = bpy.context.selected_objects[0]
imported_obj = bpy.data.objects[imported.name]
print(imported_obj)

for i in imported_obj.bound_box:
    print(i[0], i[1], i[2])

dim = imported_obj.dimensions
print(dim)

max_dim = max(max(dim.x, dim.y), dim.z) # only look at dimx dimy
scale_factor = 6/max_dim;

bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
dim = imported_obj.dimensions

# https://blender.stackexchange.com/questions/24015/how-to-place-objects-on-the-center-of-the-ground-plane-via-python
bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
imported_obj.location = (0, 0, 0)

filename, file_extension = os.path.splitext(export_png)

counter = 0
for obj in bpy.data.objects:
    if obj.type == "CAMERA":
        bpy.context.scene.render.filepath = filename+str(counter)+file_extension
        print("exporting to", bpy.context.scene.render.filepath)
        bpy.data.scenes[0].camera = obj
        bpy.ops.render.render(write_still=True)
        counter += 1
