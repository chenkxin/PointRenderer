# @Author: chenkxin
# @Date:   2023-05-13 00:07:29
# @Last Modified by:   kxchen
# @Last Modified time: 2023-05-13 00:24:59
# @Github: https://github.com/chenkxin

#!/bin/bash
# cd pics
test $# -lt 2 && die "Missing path." 1
path=$1
echo $path
cd $path
workdir=$(cd $(dirname $0); pwd)
echo $workdir
str=$(ls)
folders=(${str// / })
# mode='point2_points'
# mode='sprin_points'
# mode='sprin_points_2'
# mode='prin_points'
# mode='point_points'
mode='con_points'

for folder in ${folders[@]}
do
    echo $folder
    clas=(${folder//_/ })
    echo $(cd $(dirname $0); pwd)
    for i in {0..0}
    do
        for j in {1..1}
        do
            mitsuba $folder/$mode/mitsuba_scene_${clas}_${mode}_${i}_render_${j}.xml
        done
    done
done
