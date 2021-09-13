# -*- coding:utf-8 -*-
#   拼接图片

from PIL import Image
import numpy as np
import json
import random
import os
import base64

#   读取json地址
json_path = 'C:\\Users\\dangc\\Desktop\\a\\joint——标签替换\\trans\\\\'
#   读取图片地址
img_path = 'C:\\Users\\dangc\\Desktop\\a\\joint——标签替换\\trans\\'
#   生成图片和json地址
image_path = 'C:\\Users\\dangc\\Desktop\\a\\joint——标签替换\\image\\'
#   不更改的标签
label = ['\\bot',
         '\\measuredangle',
         '\\arrow',]
#   拼接图片地址
joint_path = 'C:\\Users\\dangc\\Desktop\\a\\joint——标签替换\\nam\\'
#   拼接的文件名，字符_数字格式，例如图片为a：a_0
nam = os.listdir(joint_path)


class Joint:

    def __init__(self, name, json_path, img_path, joint_path, image_path, label, nam):
        self.name = name
        self.json_path = json_path
        self.img_path = img_path
        self.image_path = image_path
        self.joint_path = joint_path
        self.label = label
        self.nam = nam
        self.start()

    def start(self):
        self.get_json()
        self.image = Image.open(self.img_path + self.name + '.jpg')
        # self.islable()
        if self.islable():
            self.image.save(self.image_path + self.name + '_joint.jpg')
            self.labelme['shapes'] = self.shapes
            self.labelme['imageData'] = self.base()
            self.set_json()

    def islable(self):
        array = np.array(self.label)
        print(self.name)
        a = 0
        for i in range(len(self.shapes)):
            shapes = self.shapes[i]
            if (shapes['label'] == array).any():
                continue
            else:
                a += 1
                points = shapes['points']
                x = int(points[0][0])
                y = int(points[0][1])
                x1 = int(points[1][0])
                y1 = int(points[1][1])
                if y > y1 and x < x1:
                    ww = x1 - x

                    hh = y - y1
                    y = y1
                elif x > x1 and y > y1:
                    ww = x - x1
                    hh = y - y1
                    x = x1
                    y = y1
                else:
                    ww = x1 - x
                    hh = y1 - y
                #           左上角位置               ，需要粘贴的长和高
                points = [x, y, ww, hh]
                a = random.randrange(0, len(self.nam))
                self.add_img(points, a)
                shapes['label'] = self.nam[a].split('_')[0]
        if a == 0:
            return False
        else:
            return True

    #   写json
    def set_json(self):
        if not os.path.exists(self.image_path[:-1]):
            os.makedirs(self.image_path[:-1])
        file = self.image_path + self.name + '_joint.json'
        f_obj = open(file, 'w')
        json_str = json.dumps(self.labelme)
        with open(file, 'w') as json_file:
            json_file.write(json_str)
        f_obj.close()

    def add_img(self, points, i):
        image = Image.open(self.joint_path + self.nam[i])
        image = image.resize((points[2], points[3]), Image.ANTIALIAS)
        self.image.paste(image, (points[0], points[1]), mask=None)

    # 读取json，拿到所有数据
    def get_json(self):
        jsonx = dict()
        page = []
        with open(self.json_path + self.name + '.json', 'r', encoding='utf-8') as path_json:  # gb18030
            jsonx = json.load(path_json)
        self.shapes = jsonx['shapes']
        del jsonx['shapes']
        self.labelme = jsonx

    # 将图片转换成base64
    def base(self):
        f = open(self.image_path + self.name + '_joint.jpg', 'rb')
        byteC = base64.b64encode(f.read())
        # 将base64解码成字符串
        return byteC.decode('utf-8')


json_name = os.listdir(json_path)
for i in json_name:
    if 'json' in i:
        name = i.split('.')[0]
        Joint(name, json_path, img_path, joint_path, image_path, label, nam)

'''image_open = Image.open(r'C: 102058.png')
        image = Image.open(r'C6-02 093041.png')
        print(image_open.size, image.size)
        #   合成图片
        image_open.paste(image, (1, 2), mask=None)
        #   保存图片

        #   设置图片大小
        image = image.resize((100, 100), Image.ANTIALIAS)
        print(image.size)

        image_open.paste(image, (300, 300), mask=None)
        image_open.save(r'')'''
