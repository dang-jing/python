# -*- coding:utf-8 -*-
#   labelme转vision输出
import json
import os

labelme_path = 'C:\\Users\\dangc\\Desktop\\a\\'
vision_path = 'C:\\Users\\dangc\\Desktop\\a\\'


class vision:

    def __init__(self, name, labelme_path, vision_path):
        self.name = name
        self.vision_path = vision_path
        self.labelme_path = labelme_path
        self.start()

    def start(self):
        self.get_json()
        self.isvalue()
        self.set()

    def isvalue(self):
        self.page = []
        for i in range(len(self.shapes)):
            shapes = self.shapes[i]
            if 'geometry' == shapes['label']:
                points = shapes['points']
                points = [int(points[0][0]), int(points[0][1]), int(points[1][0]), int(points[1][1])]
                self.contains('geometry', points)
            elif 'text' == shapes['label']:
                points = shapes['points']
                points = [int(points[0][0]), int(points[0][1]), int(points[1][0]), int(points[1][1])]
                self.contains('text', points)
        self.vision = dict()
        self.vision['page'] = self.page

    def set(self):
        # a = {'imageData': 'aaaaaa'}
        if not os.path.exists(self.vision_path[:-1]):
            os.makedirs(self.vision_path[:-1])
        file = self.vision_path + self.name + '_vision.json'
        f_obj = open(file, 'w')
        json_str = json.dumps(self.vision)
        with open(file, 'w') as json_file:
            json_file.write(json_str)
        f_obj.close()

    def contains(self, value, points):

        lines = []
        symbols = []
        rounds = []
        for i in self.shapes:
            if type != i['label']:
                xy = i['points']
                xy_x = xy[0][0]
                xy_y = xy[0][1]
                xy_x1 = xy[1][0]
                xy_y1 = xy[1][1]
                # 判断左上点xy是否在截图的两点坐标之内
                if points[1] - 2 < xy_y < points[3] + 2 and points[0] - 2 < xy_x < points[2] + 2 and points[
                    0] - 2 < xy_x1 < points[2] + 2 and points[1] - 2 < xy_y1 < points[3] + 2:
                    label = i['label']
                    if 'geometry' == value:
                        if 'geometry' != label:
                            if 'segmline' == label:
                                lines.append(xy)
                            elif 'round' == label:
                                rounds.append(xy)
                            else:
                                a = dict()
                                a['symbol'] = label
                                a['loc'] = [xy_x, xy_y1, xy[1][0], xy[1][1]]
                                symbols.append(a)
                    elif 'text' == value:
                        if 'text' != label:
                            page = dict()
                            page['type'] = value
                            page['content'] = label
                            page['loc'] = xy
                            self.page.append(page)
                            print(self.page)
        if 'geometry' == value:
            page = dict()
            page['type'] = value
            page['loc'] = points
            content = dict()
            content['lines'] = lines
            content['symbols'] = symbols
            content['rounds'] = rounds
            page['content'] = content
            self.page.append(page)

    def get_json(self):
        jsonx = dict()
        with open(self.labelme_path + self.name + '.json', 'r', encoding='utf-8') as path_json:  # gb18030
            jsonx = json.load(path_json)
        self.shapes = jsonx['shapes']
        self.labelme = jsonx


names = os.listdir(labelme_path)
for i in names:
    if 'json' in i:
        name = str(i).split('.')[0]
        vision(name, labelme_path, vision_path)
