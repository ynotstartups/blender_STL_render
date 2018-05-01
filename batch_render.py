import os
import shlex

REALPATH = os.path.dirname(os.path.realpath(__file__))
PYTHON_SCRIPT = os.path.join(REALPATH, 'blender_render.py')

def render(path_to_stl, blender_exec, blend_file_path, export_png, rotation):
    # hacky way of changing extension from stl to png
    command = '{} --background {} --python {} --input_model {} --export_png '+'{} '*len(export_png)
    if rotation:
        command += ' --rotation'

    command = command.format(
        *[shlex.quote(i) for i in [
        args.blender_exec,
        blend_file_path,
        PYTHON_SCRIPT,
        path_to_stl,
        *export_png
        ]]
    )

    print(command)
    os.system(command)


if __name__ == "__main__":
    # TODO: add test
    # 1. tinkercad render should output 1 picture
    # 2. non-tinkercad render should returns 6 pictures

    import sys
    if sys.version_info < (3, 3):
        print('You need to run this with at least Python 3.3')
        sys.exit(1)

    import argparse

    parser = argparse.ArgumentParser(description="Batch Render STL file with blender")
    parser.add_argument("--blender_exec", required=True, help="Path to Blender Executable")
    parser.add_argument("--export_png", nargs='+', required=True, help="the directory the render will export to, if the directory doesn't exist will try to create it")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--stl_file", help="the one stl file you want to render")
    group.add_argument("--stl_dir", help="the directory of stl files you want to render")

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--general", help="You want to render non-tinkercad objects", action="store_true", default=True)
    group.add_argument("--tinkercad", help="You want to render tinkercad objects", action="store_true")

    args = parser.parse_args()

    if args.tinkercad:
        assert len(args.export_png) == 1, "length of export_png should be 1 instead of {}".format(len(args.export_png))
        rotation = False
        blend_file_path = os.path.join(REALPATH, "blend", 'tinkercad_camera_track_to.blend')
    elif args.general:
        assert len(args.export_png) == 6, "length of export_png should be 6 instead of {}".format(len(args.export_png))
        rotation = True
        blend_file_path = os.path.join(REALPATH, "blend", 'layers_irregular_surface.blend')
    else:
        raise ValueError("This should not never happen")

    if args.stl_dir is not None:
        files = os.listdir(args.stl_dir)
        for name in files:
            if name.lower().endswith(".stl"):
                stl_name = name
                render(
                    os.path.join(args.stl_dir, stl_name),
                    args.blender_exec,
                    blend_file_path,
                    args.export_png,
                    rotation
                )
    elif args.stl_file is not None:
        render(
            args.stl_file,
            args.blender_exec,
            blend_file_path,
            args.export_png,
            rotation
        )
    else:
        print("Wrong Usage, This should never happens")
