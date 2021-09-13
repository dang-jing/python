# -*_coding:utf8-*-

import json
from PIL import Image
import cv2
import numpy as np
import base64
import os

# 读取json地址
jsonPath = "C:\\Users\\dangc\\Desktop\\a\\single\\json\\"
# 写入子json地址
sonjsonpath = 'C:\\Users\\dangc\\Desktop\\a\\single\\newjson\\'
#  需要截取的table
value = 's'
# 原图地址
imgpath = "C:\\Users\\dangc\\Desktop\\a\\single\\img\\"
# 截取图片存放地址
splitimg = 'C:\\Users\\dangc\\Desktop\\a\\single\\newimg\\'


class splitLabel(object):
    def __init__(self, json_Name):
        # 拿到当前文件名
        self.name = json_Name
        self.img_name = self.name + '.jpg'
        self.start()

    def start(self):
        self.get_json()
        # print(self.shapes)
        self.isValue()
        # print(self.points)
        # 遍历需要切分的位置
        for i in range(len(self.points)):
            if '_' in self.name:
                self.name = '{}{}{}'.format(self.name.split('_')[0], '_', i + 1)
            else:
                self.name = '{}{}{}'.format(self.name, '_', i + 1)
            # print(self.points[i])
            point = self.points[i]
            self.split(point)
            self.set_json(point)

    # 写子json数据
    def set_json(self, point):
        y = point[1]
        x = point[0]
        y1 = point[3]
        x1 = point[2]
        son_shapes = []
        for i in self.shapes:
            xy = i['points']
            if value not in i['label']:
                xy_x = xy[0][0]
                xy_y1 = xy[0][1]
                xy_y2 = xy[1][1]
                # 判断左上点xy是否在截图的两点坐标之内
                if y - 2 < xy_y1 < y1 + 2 and x - 2 < xy_x < x1 + 2:
                    # print(x, y)
                    # print(xy)
                    # 修改标注后截取位置
                    xy[0][0] = xy[0][0] - x
                    xy[0][1] = xy_y1 - y
                    xy[1][0] = xy[1][0] - x
                    xy[1][1] = xy_y2 - y
                    son_shapes.append(i)
        self.labelme.pop('shapes')
        self.labelme['shapes'] = son_shapes
        self.labelme.pop('imageHeight')
        self.labelme.pop('imageWidth')
        self.labelme.pop('imageData')
        self.labelme['imageData'] = self.base()
        img = Image.open(imgpath + self.img_name)
        self.labelme['imageHeight'] = img.height
        self.labelme['imageWidth'] = img.width
        self.set()

    # 将图片转换成base64
    def base(self):
        a=self.iii
        print(a)
        f = open(a, 'rb')
        byteC = base64.b64encode(f.read())
        # 将base64解码成字符串
        return byteC.decode('utf-8')

    # 对json文件写入数据
    def set(self):
        # a = {'imageData': 'aaaaaa'}
        if not os.path.exists(sonjsonpath[:-1]):
            os.makedirs(sonjsonpath[:-1])
        file = sonjsonpath + self.name + '.json'
        f_obj = open(file, 'w')
        json_str = json.dumps(self.labelme)
        with open(file, 'w') as json_file:
            json_file.write(json_str)
        f_obj.close()

    # 根据四点坐标切分图片
    def split(self, point):
        x = point[0]
        y = point[1]
        x1 = point[2]
        y1 = point[3]
        img = cv2.imdecode(np.fromfile(imgpath + self.img_name, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        ROI = img[y:y1, x:x1]
        # 判断文件夹路径是否存在
        if not os.path.exists(splitimg[:-1]):
            os.makedirs(splitimg[:-1])
        if ROI.size != 0:
            str = splitimg + self.name + ".jpg"
            cv2.imencode('.jpg', ROI)[1].tofile(str)
            self.iii = str

    # 拿到所有要切分的位置
    def isValue(self):
        points = []
        for i in range(len(self.shapes)):
            shapes = self.shapes[i]
            point = []
            if value in shapes['label']:
                a = shapes['points']
                point.append(int(a[0][0]))
                point.append(int(a[0][1]))
                point.append(int(a[1][0]))
                point.append(int(a[1][1]))
                points.append(point)
        self.points = points

    # 读取json，拿到所有数据
    def get_json(self):
        jsonx = dict()
        page = []
        with open(jsonPath + self.name + '.json', 'r', encoding='utf-8') as path_json:  # gb18030
            jsonx = json.load(path_json)
        self.shapes = jsonx['shapes']
        self.labelme = jsonx


# 拿到路径下所有文件名
json_Name = os.listdir(jsonPath)
for name in json_Name:
    if 'json' in name:
        split___ = str(name).split(".")[0]
        if os.path.exists(imgpath + split___ + '.jpg'):
            splitLabel(split___)
#splitLabel('24036ef50d904727990ef2629f5cb6f7')

# splitLabel("image1.png")
#print(os.path.exists(r"C:\Users\dangc\Desktop\a\a\0a28d2ca-c59e-11eb-8206-9c2976e90c22.json"))
