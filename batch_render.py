import os
import shlex

REALPATH = os.path.dirname(os.path.realpath(__file__))
BLEND_FILE_PATH = os.path.join(REALPATH, "blend", 'tinkercad.blend')
PYTHON_SCRIPT = os.path.join(REALPATH, 'blender_render.py')

def render(path_to_stl, blender_exec, export_dir):
    # hacky way of changing extension from stl to png
    export_png = os.path.join(
        export_dir, os.path.splitext(os.path.basename(path_to_stl))[0] + ".png"
    )

    command = '{} --background {} --python {} {} {}'.format(
        *[shlex.quote(i) for i in [
        args.blender_exec,
        BLEND_FILE_PATH,
        PYTHON_SCRIPT,
        path_to_stl,
        export_png
        ]]
    )

    print(command)
    os.system(command)


if __name__ == "__main__":
    import sys
    if sys.version_info < (3, 3):
        print('You need to run this with at least Python 3.3')
        sys.exit(1)

    import argparse

    parser = argparse.ArgumentParser(description="Batch Render STL file with blender")
    parser.add_argument("--blender_exec", required=True, help="Path to Blender Executable")
    parser.add_argument("--export_dir", required=True, help="the directory the render will export to, if the directory doesn't exist will try to create it")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--stl_file", help="the one stl file you want to render")
    group.add_argument("--stl_dir", help="the directory of stl files you want to render")

    args = parser.parse_args()

    if args.stl_dir is not None:
        files = os.listdir(args.stl_dir)
        for name in files:
            if name.lower().endswith(".stl"):
                stl_name = name
                render(
                    os.path.join(args.stl_dir, stl_name),
                    args.blender_exec,
                    args.export_dir
                )
    elif args.stl_file is not None:
        render(
            args.stl_file,
            args.blender_exec,
            args.export_dir
        )
    else:
        print("Wrong Usage, This should never happens")
