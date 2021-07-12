# -*- coding:utf-8 -*-
# labelme转jmeter

import json
import os
from json.decoder import JSONDecodeError

labelme_path = 'D:\\工作\\input\\'
# 文件夹分隔符
path_separator = "\\"
#保存地址，文件夹固定jmeter
jmeter_path = r'D:\图片'+ path_separator + "output"



class jmeter(object):

    def __init__(self, filename):
        self.name = filename
        self.labelme_json()

    def labelme_json(self):
        jsonx = dict()
        page = []

        with open(labelme_path + self.name, 'r', encoding='utf-8') as path_json:  # gb18030
            jsonx = json.load(path_json)
        #print(jsonx[''])
        '''with open(labelme_path + self.name,'r', encoding='utf-8') as conn_file:
            conn_doc = conn_file.read()
        jsonx = self.permissive_json_loads(conn_doc)'''
        shapes = jsonx['shapes']
        jmeter_json = dict()
        text_y1 = text_y2 = 0
        for i in range(len(shapes)):
            num = shapes[i]
            if 'text' in num['label']:
                text_y1 = int(num['points'][0][1])
                text_y2 = int(num['points'][1][1])
            else:
                a = dict()
                y1 = num['points'][0][1]
                y2 = num['points'][1][1]

                if text_y1 - 2 <= y1 <= text_y2 + 2 and text_y1 - 2 <= y2 <= text_y2 + 3 :
                    a['loc'] = [float(int(num['points'][0][0])), float(int(y1)), float(int(num['points'][1][0])),
                                float(int(y2))]
                    a['type'] = 'text'
                    a['content'] = num['label']
                    page.append(a)
        jmeter_json['sectionnum'] = len(page)
        jmeter_json['page'] = page
        self.jmeter_json = jmeter_json
        self.set()

    def permissive_json_loads(self,text):
        while True:
            try:
                data = json.loads(text)
            except JSONDecodeError as exc:
                if exc.msg == 'Invalid \\escape':
                    text = text[:exc.pos] + '\\' + text[exc.pos:]
                else:
                    raise
            else:
                return data

    # 对json文件写入数据
    def set(self):
        # a = {'imageData': 'aaaaaa'}
        # 判断路径是否存在，如果没有这个path则直接创建
        if not os.path.exists(jmeter_path):
            os.makedirs(jmeter_path)
        json_str = json.dumps(self.jmeter_json, ensure_ascii=False)
        with open(jmeter_path + path_separator + self.name, 'w', encoding='utf-8') as json_file:
            json_file.write(json_str)


labelme_name = os.listdir(labelme_path)
print(labelme_name)
for filename in labelme_name:
    print(filename)
    try:
        jmeter(filename)
    except JSONDecodeError as exc:
        print(filename+"获取失败")
        continue





'''with open(r'D:\工作\input\img10.json') as conn_file:
    conn_doc = conn_file.read()
conn = permissive_json_loads(conn_doc)
print(type(conn))'''
#meter('img10.json')