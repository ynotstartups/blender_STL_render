render_folder='./test/render'

# for tinkercad
test_png='./test/render/test.png'

# for general
test0_png='./test/render/test0.png'
test1_png='./test/render/test1.png'
test2_png='./test/render/test2.png'
test3_png='./test/render/test3.png'
test4_png='./test/render/test4.png'
test5_png='./test/render/test5.png'

rm $test_png $test0_png $test1_png $test2_png $test3_png $test4_png $test5_png

python3 batch_render.py --stl_file './test/test.stl'  --blender_exec '../blender-2.79-linux-glibc219-x86_64/blender' --tinkercad --export_png $test_png >/dev/null

if [ -f $test_png ]
then
    echo "tinkercad render pass\n"
else
    echo "tinkercad render fail\n"
    exit 1
fi

python3 batch_render.py --stl_file './test/azura-01.stl'  --blender_exec '../blender-2.79-linux-glibc219-x86_64/blender' --general --export_png $test0_png $test1_png $test2_png $test3_png $test4_png $test5_png 

if [ -f $test0_png ] && [ -f $test1_png ] && [ -f $test2_png ] && [ -f $test3_png ] && [ -f $test4_png ] && [ -f $test5_png ]
then
    echo "general render pass\n"
else
    echo "general render fail\n"
    exit 1
fi
