# -*- coding: utf-8 -*-
# @Author: chenkxin
# @Date:   2022-08-09 21:22:46
# @Last Modified by:   kxchen
# @Last Modified time: 2023-05-13 00:24:52
# @Github: https://github.com/chenkxin

# 此脚本用于RGB颜色和16进制颜色之间进行格式转换

from PIL import Image

# RGB格式颜色转换为16进制颜色格式
def RGB_to_Hex(rgb):
    RGB = rgb.split(',')  # 将RGB格式划分开来
    color = '#'
    for i in RGB:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').upper()
    print(color)
    return color


# 16进制颜色格式颜色转换为RGB格式
def Hex_to_RGB(hex):
    r = int(hex[1:3], 16) / 255
    g = int(hex[3:5], 16) / 255
    b = int(hex[5:7], 16) / 255
    rgb = str(r) + ',' + str(g) + ',' + str(b)
    print(rgb)
    return rgb

if __name__ == '__main__':
    Hex_to_RGB('#0ED193')
