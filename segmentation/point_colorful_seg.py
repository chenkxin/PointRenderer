# -*- coding: utf-8 -*-
# @Author: chenkxin
# @Date:   2022-08-08 21:24:46
# @Last Modified by:   kxchen
# @Last Modified time: 2023-05-13 00:24:41
# @Github: https://github.com/chenkxin

import numpy as np
import os
import geometry

# 此函数是为了使点云模型紧凑表示，更加美观，可根据渲染需要选择使用
def standardize_bbox(pcl, points_per_object):
    # pt_indices = np.random.choice(pcl.shape[0], points_per_object, replace=False)
    # np.random.shuffle(pt_indices)
    # pcl = pcl[pt_indices] # n by 3
    mins = np.amin(pcl, axis=0)
    maxs = np.amax(pcl, axis=0)
    center = ( mins + maxs ) / 2.
    scale = np.amax(maxs-mins)
    print("Center: {}, Scale: {}".format(center, scale))
    result = ((pcl - center)/scale).astype(np.float32) # [-0.5, 0.5]
    return result


# # #################################   mitsuba-0.6.0 version   ##############################################
xml_head = \
"""
<scene version="0.6.0">
    <integrator type="path">
        <integer name="maxDepth" value="-1"/>
    </integrator>
    <sensor type="perspective">
        <float name="farClip" value="100"/>
        <float name="nearClip" value="0.1"/>
        <transform name="toWorld">
            <lookat origin="3,3,3" target="0,0,0" up="0,0,1"/>
        </transform>
        <float name="fov" value="25"/>

        <sampler type="ldsampler">
            <integer name="sampleCount" value="256"/>
        </sampler>
        <film type="ldrfilm">
            <integer name="width" value="1600"/>
            <integer name="height" value="1200"/>
            <rfilter type="gaussian"/>
            <boolean name="banner" value="false"/>
        </film>
    </sensor>

    <bsdf type="roughplastic" id="surfaceMaterial">
        <string name="distribution" value="ggx"/>
        <float name="alpha" value="0.05"/>
        <float name="intIOR" value="1.46"/>
        <rgb name="diffuseReflectance" value="1,1,1"/> <!-- default 0.5 -->
    </bsdf>

"""

xml_ball_segment = \
"""
    <shape type="sphere">
        <float name="radius" value="0.025"/>
        <transform name="toWorld">
            <translate x="{}" y="{}" z="{}"/>
        </transform>
        <bsdf type="diffuse">
            <rgb name="reflectance" value="{},{},{}"/>
        </bsdf>
    </shape>
"""

xml_tail = \
"""
    <shape type="rectangle">
        <ref name="bsdf" id="surfaceMaterial"/>
        <transform name="toWorld">
            <scale x="10" y="10" z="1"/>
            <translate x="0" y="0" z="-0.5"/>
        </transform>
    </shape>

    <shape type="rectangle">
        <transform name="toWorld">
            <scale x="10" y="10" z="1"/>
            <lookat origin="-4,4,20" target="0,0,0" up="0,0,1"/>
        </transform>
        <emitter type="area">
            <rgb name="radiance" value="6,6,6"/>
        </emitter>
    </shape>
</scene>
"""



################################   mitsuba-2 version   ##############################################
# xml_head = \
# """
# <scene version="2.2.1">
#     <integrator type="path">
#         <integer name="max_depth" value="-1"/>
#     </integrator>
#     <sensor type="perspective">
#         <float name="far_clip" value="100"/>
#         <float name="near_clip" value="0.1"/>
#         <transform name="to_world">
#             <lookat origin="3,3,3" target="0,0,0" up="0,0,1"/>
#         </transform>
#         <float name="fov" value="25"/>
#
#         <sampler type="ldsampler">
#             <integer name="sample_count" value="256"/>
#         </sampler>
#         <film type="hdrfilm">
#             <integer name="width" value="1600"/>
#             <integer name="height" value="1200"/>
#             <rfilter type="gaussian"/>
#             <boolean name="banner" value="false"/>
#         </film>
#     </sensor>
#
#     <bsdf type="roughplastic" id="surfaceMaterial">
#         <string name="distribution" value="ggx"/>
#         <float name="alpha" value="0.05"/>
#         <float name="int_ior" value="1.46"/>
#         <rgb name="diffuse_reflectance" value="1,1,1"/> <!-- default 0.5 -->
#     </bsdf>
#
# """
#
# xml_ball_segment = \
# """
#     <shape type="sphere">
#         <float name="radius" value="0.025"/>
#         <transform name="to_world">
#             <translate x="{}" y="{}" z="{}"/>
#         </transform>
#         <bsdf type="diffuse">
#             <rgb name="reflectance" value="{},{},{}"/>
#         </bsdf>
#     </shape>
# """
#
# xml_tail = \
# """
#     <shape type="rectangle">
#         <ref name="bsdf" id="surfaceMaterial"/>
#         <transform name="to_world">
#             <scale x="10" y="10" z="1"/>
#             <translate x="0" y="0" z="-0.5"/>
#         </transform>
#     </shape>
#
#     <shape type="rectangle">
#         <transform name="to_world">
#             <scale x="10" y="10" z="1"/>
#             <lookat origin="-4,4,20" target="0,0,0" up="0,0,1"/>
#         </transform>
#         <emitter type="area">
#             <rgb name="radiance" value="6,6,6"/>
#         </emitter>
#     </shape>
# </scene>
# """

def colormap(x,y,z):
    vec = np.array([x,y,z])
    vec = np.clip(vec, 0.001,1.0)
    norm = np.sqrt(np.sum(vec**2))
    vec /= norm
    return [vec[0], vec[1], vec[2]]

################ version 1 ####################
cmap = np.array([
    [0.1411764705882353, 0.5137254901960784, 0.6666666666666666],
    [0.6588235294117647, 0.9568627450980393, 0.20392156862745098],
    [0.3686274509803922, 1.0, 0.7254901960784313],
    [0.49411764705882355, 0.00392156862745098, 0.6862745098039216],
    [0.7137254901960784, 0.8745098039215686, 0.8470588235294118],
    [0.6352941176470588, 0.4196078431372549, 0.48627450980392156],
    [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
    [3.12493437e-02, 1.00000000e+00, 1.31250131e-06],
    [0.00000000e+00, 6.25019688e-02, 1.00000000e+00],
    [1.00000000e+00, 0.00000000e+00, 9.37500000e-02],
    ])

################ version 2 ####################
# cmap = np.array([
#     [0.3607843137254902,0.4196078431372549,0.7529411764705882], # b
#     [1.0,0.6549019607843137,0.14901960784313725], # yellow
#     [0.3686274509803922, 1.0, 0.7254901960784313],  # light blue
#     [0.4823529411764706,0.9686274509803922,0.40784313725490196], # g
#     [0.6352941176470588, 0.4196078431372549, 0.48627450980392156], # pink
#     [0.7137254901960784, 0.8745098039215686, 0.8470588235294118], # gray
#     [0.1411764705882353, 0.5137254901960784, 0.6666666666666666],# blue
#     [0.6588235294117647, 0.9568627450980393, 0.20392156862745098], # green
#     [0.49411764705882355, 0.00392156862745098, 0.6862745098039216],  # purple
#     [1.00000000e+00, 0.00000000e+00, 0.00000000e+00], # deep red
#     [3.12493437e-02, 1.00000000e+00, 1.31250131e-06], # deep green
#     [0.00000000e+00, 6.25019688e-02, 1.00000000e+00],
#     [1.00000000e+00, 0.00000000e+00, 9.37500000e-02],
#     ])

# 获取类别
cls_list = ["Airplane", "Bag", "Cap", "Car", "Chair", "Earphone", "Guitar", "Knife", "Lamp", "Laptop", "Motorbike", "Mug", "Pistol", "Rocket", "Skateboard", "Table"]

cls_start_dist = {
    "Airplane": 0,
    "Bag": 341,
    "Cap": 355,
    "Car": 366,
    "Chair": 524,
    "Earphone": 1228,
    "Guitar": 1242,
    "Knife": 1401,
    "Lamp": 1481,
    "Laptop": 1767,
    "Motorbike": 1850,
    "Mug": 1901,
    "Pistol": 1939,
    "Rocket": 1983,
    "Skateboard": 1995,
    "Table": 2026
}
cls_start = [ 0, 341, 355, 366, 524, 1228, 1242, 1401, 1481, 1767, 1850, 1901, 1939, 1983, 1995, 2026 ]

def WriteRenderXML(rot_mat=None, path1="pics", pcl=None, render_mode=0, seg_id=0, idx="0", clas="pic", seg=None, mode="seg"):
    if pcl is None:
        exit(0)
    xml_segments = [xml_head]
    if not os.path.exists(path1):
        os.mkdir(path1)
    path2 = "{}/{}_{}".format(path1, clas, idx)
    if not os.path.exists(path2):
        os.mkdir(path2)
    path = "{}/{}".format(path2, mode)
    if not os.path.exists(path):
        os.mkdir(path)

    pcl = standardize_bbox(pcl, 2048)
    pcl = pcl[:,[2,0,1]]
    pcl[:,0] *= -1
    pcl[:,2] += 0.0125

    if rot_mat is not None:
        pcl = pcl.dot(rot_mat)

    if seg is None:
        seg = np.zeros((2048,), dtype = int)
    gt = cmap[seg, :]
    for i in range(pcl.shape[0]):
        if render_mode == 0:
            # 颜色线性变化渲染
            color = colormap(pcl[i, 0] + 0.5, pcl[i, 1] + 0.5, pcl[i, 2] + 0.5 - 0.0125)
        elif render_mode == 1:
            # 颜色按照传入的 cmap 渲染
            color = colormap(gt[i][0], gt[i][1], gt[i][2])
        xml_segments.append(xml_ball_segment.format(pcl[i, 0], pcl[i, 1], pcl[i, 2], *color))
    xml_segments.append(xml_tail)

    xml_content = str.join('', xml_segments)

    with open('{}/mitsuba_scene_{}_{}_{}_render_{}.xml'.format(path, clas, mode, seg_id, render_mode), 'w') as f:
        f.write(xml_content)

if __name__ == '__main__':
    rot_mat_1 = np.load("rot_mat_1.npy")[0]
    rot_mat_2 = np.load("rot_mat_2.npy")[0]
    rot_mat_3 = np.load("rot_mat_3.npy")[0]
    rot_mats = [
        None,
        rot_mat_1,
        rot_mat_2,
        rot_mat_3
    ]
    # train_models 是指多个不同训练模型，可以是不同网络或者不同参数等，将需要对比的模型的实验数据放到指定目录下，并将模型名称添加进下面列表
    train_models = ['con_points', 'point2_points', 'prin_points', 'sprin_points', 'point_points']
    segName = "seg1"
    for t in range(len(train_models)):
        train_model = train_models[t]
        # 读取点云模型
        point_set = np.load('{}/{}/16_nr_points.npy'.format(segName, train_model), allow_pickle=True)
        # 读取预测分割类别值
        pred_seg = np.load('{}/{}/16_pred_seg.npy'.format(segName, train_model), allow_pickle=True)
        # 读取标准分割类别值
        gt = np.load('{}/{}/16_gt_seg.npy'.format(segName, train_model), allow_pickle=True)
        seg_classes = {'Earphone': [16, 17, 18], 'Motorbike': [30, 31, 32, 33, 34, 35], 'Rocket': [41, 42, 43],
                       'Car': [8, 9, 10, 11], 'Laptop': [28, 29], 'Cap': [6, 7], 'Skateboard': [44, 45, 46],
                       'Mug': [36, 37],
                       'Guitar': [19, 20, 21], 'Bag': [4, 5], 'Lamp': [24, 25, 26, 27], 'Table': [47, 48, 49],
                       'Airplane': [0, 1, 2, 3], 'Pistol': [38, 39, 40], 'Chair': [12, 13, 14, 15], 'Knife': [22, 23]}

        # shapenet 有 16 个大类
        for j in range(16):
            idx = cls_start[j]
            p_seg = pred_seg[j][j]
            clas = cls_list[j]

            # choice 是一定的， 这样就可以在之后的多次修改旋转角度等重新渲染时， 能够对同一个模型点集的同样的点分布进行操作
            choice = np.load("pics/{}_{}/rot/{}_choice.npy".format(clas, idx, clas))

            seg_gt = gt[j][j]
            pcl = point_set[j][j][choice, 0:3]
            pcl = np.asarray(pcl)

            # 这里的循环是为了切换分割模式
            for i in range(2):
                # i = 1
                if i == 0:
                    # 默认分割模式，groud truth
                    seg = seg_gt
                elif i == 1:
                    # 预测分割模式，predict segmentation
                    seg = p_seg
                seg = seg[choice]
                seg = seg - seg.min()

                # 下面是一些旋转矩阵，可供调试使用
                # 绕 x轴 30°
                # rot = [[1.0000000, 0.0000000, 0.0000000],
                # [0.0000000, 0.1542515, 0.9880316],
                # [0.0000000, -0.9880316, 0.1542515]]
                # 绕 y轴 30°，看起来是垂直在转
                # rot = [[  0.1542515,  0.0000000, -0.9880316],
                # [0.0000000,  1.0000000,  0.0000000],
                # [0.9880316,  0.0000000,  0.1542515]]
                # 绕 z轴 30°，看起来是水平在转
                # rot = [[0.1542515, 0.9880316, 0.0000000],
                # [-0.9880316, 0.1542515, 0.0000000],
                # [0.0000000, 0.0000000, 1.0000000]]

                # 添加旋转操作
                WriteRenderXML(rot_mat=rot_mats[3], path1="test_seg-mitsuba-1-png", pcl=pcl, render_mode=1, seg_id=i, idx=idx, clas=clas, seg=seg, mode=train_model)
                