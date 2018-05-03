import bpy
import os
import sys
import math

import argparse
parser = argparse.ArgumentParser(description="Render STL file with blender")
parser.add_argument("--export_png",
        nargs='+',
        required=True,
        help="the directory the render will export to, if the directory doesn't exist will try to create it"
)

parser.add_argument("--input_model",
        required=True,
        help="Path to input 3d mesh")

parser.add_argument("--rotation",
        default=False,
        action="store_true",
        required=False,
        help="Whether to render in 6 angles default is false, do this for non-tinkercad render")

args, unknown = parser.parse_known_args()

input_model = args.input_model
export_png = args.export_png

assert input_model.lower().endswith("stl")
assert all([i.lower().endswith("png") for i in export_png])

scene = bpy.context.scene
bpy.ops.import_mesh.stl(filepath=input_model)

imported = bpy.context.selected_objects[0]
imported_stl = bpy.data.objects[imported.name]
dim = imported_stl.dimensions
max_dim = max(max(dim.x, dim.y), dim.z) # only look at dimx dimy
scale_factor = 6/max_dim;

bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
dim = imported_stl.dimensions

# https://blender.stackexchange.com/questions/24015/how-to-place-objects-on-the-center-of-the-ground-plane-via-python
bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN", center="BOUNDS")
imported_stl.location = (0, 0, 0)

material = bpy.data.materials.get("Material")
imported_stl.data.materials.append(material)

rotation_eulers = [
    (0, 0, 0),
    (0, 0, math.pi/2),
    (0, 0, 2*math.pi/2),
    (0, 0, 3*math.pi/2),
    (math.pi/2, 0, 0),
    (-math.pi/2, 0, 0),
]

counter = 0
for obj in bpy.data.objects: # used for multiple cameras
    if obj.type == "CAMERA":
        # 6 rotation
        if args.rotation:
            assert len(export_png) == 6, "length of export_png should be 6 for rotation"
            for rotation_euler, filepath in zip(rotation_eulers, args.export_png):
                bpy.context.scene.render.filepath = filepath
                imported_stl.rotation_euler = rotation_euler
                bpy.ops.render.render(write_still=True)
                counter += 1
        else:
            assert len(export_png) == 1, "length of export_png should be 1 for rotation"
            # no rotation
            bpy.data.scenes[0].camera = obj
            obj.constraints['Track To'].target = imported_stl

            bpy.context.scene.render.filepath = export_png[0] # we know length is 1
            bpy.ops.render.render(write_still=True)
