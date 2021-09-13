# -*- coding:utf-8 -*-

import codecs
import json
import base64
from PIL import Image

#   line识别地址
line_path = r'C:\Users\dangc\Desktop\a\2_graph_labeled党\Label.txt'
#   图片地址
img_path = 'C:\\Users\\dangc\\Desktop\\a\\2_graph_labeled党\\'
#   labelme的json数据
label_json = 'C:\\Users\\dangc\\Desktop\\a\\2_graph_labeled党\\2_graph_labeled\\'

def start():
    get_txt()


def get_txt():
    for line in open(line_path, 'r', encoding='UTF-8'):
        a = line.split('\t')
        name = a[0].split('/')[1]
        line_txt = json.loads(a[1])
        labelme = parsing_json(line_txt)
        image_path = img_path + name
        image = Image.open(image_path)
        labelme['imageHeight'] = image.height
        labelme['imageWidth'] = image.width
        labelme['imageData'] = base(image_path)
        labelme['imagePath'] = '../'+name
        json_str = json.dumps(labelme, ensure_ascii=False)
        with open(label_json+name[:-4]+'.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_str)

def base(image_path):
    f = open(image_path, 'rb')
    byteC = base64.b64encode(f.read())
    # 将base64解码成字符串
    return byteC.decode('utf-8')


def parsing_json(line_txt):
    labelme = dict()
    labelme['version'] = '4.5.9'
    labelme['flags'] = {}

    shapes = []
    for i in line_txt:
        shape = dict()
        points = i['points']
        shape['label'] = '@' + str(len(i['transcription']))
        shape['points'] = [[float(points[0][0]), float(points[0][1])], [float(points[2][0]), float(points[2][1])]]
        shape['group_id'] = None
        shape['shape_type'] = 'rectangle'
        shape['flags'] = {}
        shape['contions'] = i['transcription']
        shapes.append(shape)
    labelme['shapes'] = shapes
    return labelme


if __name__ == '__main__':
    start()
