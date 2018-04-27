import os

BLENDER_PATH = "/home/mmf159/Documents/blender-2.79-linux-glibc219-x86_64/blender"
STL_DIR = '/home/mmf159/Downloads/tinkercad_render'
# BLEND_FILE_PATH = '/home/mmf159/Documents/blender_testing/Softlights_original_llight_position_changed_and_background_perpective_camera.blend'
BLEND_FILE_PATH = '/home/mmf159/Documents/blender_testing/tinkercad.blend'
PYTHON_SCRIPT = '/home/mmf159/Documents/blender_testing/blender_render.py'

files = os.listdir(STL_DIR)
for name in files[:1000]:
    if name.lower().endswith(".stl"):
        stl_name = name
        export_png = os.path.splitext(stl_name)[0] + ".png"

        # ./blender --background '/home/mmf159/Downloads/Softlights-less.blend' --python ~/Documents/blender_testing/blender_render.py '/home/mmf159/Downloads/jfkbust.stl'  '/home/mmf159/Downloads/0.png'
        command = '{} --background "{}" --python "{}" \"{}\" \"{}\"'.format(
            BLENDER_PATH, BLEND_FILE_PATH, PYTHON_SCRIPT,
            os.path.join(STL_DIR, stl_name),
            os.path.join(STL_DIR, "blender_render", export_png)
        )

        print(command)
        print("------------------- system---------------------")
        os.system(command)
        print("------------------- system---------------------")
