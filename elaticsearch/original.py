# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
import base64
import uuid
import json
import os

img_paths = 'D:\\测试\\中考\\imgs\\no_answer\\'
json_path = 'D:\\测试\\中考\\img_json\\no_answer\\'


class original():
    def __init__(self):
        list_json = os.listdir(img_paths)
        for i in list_json:
            self.name = i.split('.')[0]
            self.img_name = i
            self.get_json()
        '''self.name = list_json[0].split('.')[0]
        self.img_name = list_json[0]
        self.get_json()'''

    def get_json(self):
        self.data = dict()
        with open(json_path + self.name + '.json', 'r', encoding='utf-8') as path_json:  # gb18030
            self.data['original_json'] = json.load(path_json)
        self.base()
        #print(self.data)
        self.link()

    # 将图片转换成base64
    def base(self):
        f = open(img_paths + self.img_name, 'rb')
        byteC = base64.b64encode(f.read())
        # 将base64解码成字符串
        f.close()
        self.data['original_json']['imageData'] = byteC.decode('utf-8')

    def link(self):
        es = Elasticsearch(['192.168.3.10:9200'])
        print(es.index(index='original_data', doc_type='doc', id=self.name, body=self.data))
        # print(es.get(index='py2', doc_type='doc', id=1))


# list_json = os.listdir(img_paths)
'''for i in list_json:
    original(i)'''
original()
