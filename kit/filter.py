# -*- coding:utf-8 -*-
#   局部，精确拿到

import json
import os

json_path = 'D:\\测试\\中考\\imgs\\共享\\中考网\\typeset\\SSD Train1\\3_graph_labeled\\'
#   写入json
fil_path = 'D:\\测试\\测试\\'
#   指定label标签
value = '0'
#   获取类型：1为拿开头，2为去（过滤掉）开头，3为精确拿到
select = 1


class filter:

    def __init__(self, json_name, json_path, fil_parth, value, select):
        self.name = json_name
        self.path = json_path
        self.fil_path = fil_parth
        self.value = value
        self.select = select
        self.start()

    def start(self):
        self.get_json()
        self.isValue()
        self.set_json()

#   写json
    def set_json(self):
        if not os.path.exists(self.fil_path[:-1]):
            os.makedirs(self.fil_path[:-1])
        file = self.fil_path + self.name + '_filter_' + self.value + '.json'
        f_obj = open(file, 'w')
        json_str = json.dumps(self.labelme)
        with open(file, 'w') as json_file:
            json_file.write(json_str)
        f_obj.close()

#   读json
    def get_json(self):
        jsonx = dict
        with open(self.path + self.name + '.json', 'r', encoding='utf-8') as path_json:
            jsonx = json.load(path_json)
        self.shapes = jsonx['shapes']
        del jsonx['shapes']
        self.labelme = jsonx

#   获取过滤标签
    def isValue(self):
        points = []
        for i in range(len(self.shapes)):
            shapes = self.shapes[i]
            if self.select == 1:
                if self.value == shapes['label'][0]:
                    points.append(shapes)
            elif self.select == 2:
                if self.value != shapes['label'][0]:
                    points.append(shapes)
            elif self.select == 3:
                if self.value == shapes['label']:
                    points.append(shapes)
        #   后续多个判断值使用
        #   判断数组是否含有1,True
        # if (shapes['label'] == self.value).any():
        self.labelme['shapes'] = points


names = os.listdir(json_path)
for i in names:
    if 'json' in i:
        name = i.split('.')[0]
        filter(name, json_path, fil_path, value, select)
