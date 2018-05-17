Batch render STL file with Blender

Require [Blender](https://www.blender.org/)
```
python3 batch_render.py -h
usage: batch_render.py [-h] --blender_exec BLENDER_EXEC --export_dir
                       EXPORT_DIR (--stl_file STL_FILE | --stl_dir STL_DIR)

Batch Render STL file with blender

optional arguments:
  -h, --help            show this help message and exit
  --blender_exec BLENDER_EXEC
                        Path to Blender Executable
  --export_dir EXPORT_DIR
                        the directory the render will export to, if the
                        directory doesn't exist will try to create it
  --stl_file STL_FILE   the one stl file you want to render
  --stl_dir STL_DIR     the directory of stl files you want to render
```
![Example Image](example/drethraider0.jpg)

![Example Image](example/incredible-wluff-wolt0.png)
