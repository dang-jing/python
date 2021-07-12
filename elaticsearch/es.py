# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
import base64
import uuid
import os

img_paths = r'C:\Users\dangc\Desktop\b\1400\\'


def link(id, body):
    es = Elasticsearch(['192.168.3.10:9200'])
    print(es.index(index='dataset', doc_type='doc', id=id, body=body))
    # print(es.get(index='py2', doc_type='doc', id=1))


def img_json(img_path, txtlist):
    body = dict()
    body['question_types'] = '解答题'
    body['topic _type'] = '1400标准题'
    body['subject_quality'] = '仅题目相关'
    body['topic_hierarchy'] = '单题目'
    body['txt_graph'] = '一文本零图'
    body['is_answer'] = '无答案'
    body['picture_type'] = '标准截图'
    body['picture_quality'] = '合格'
    print(img_path)
    b = int(img_path.split("\\")[-1].split(".")[0][3:])
    body['txt'] = txtlist[b - 1]
    # print(c)
    img(body, img_path)


def img(body, img_path):
    label = dict()
    str = base(img_path)
    id = uuid.uuid1()
    label['imagePath'] = '{}{}'.format(id, '.jpg')
    label['imageData'] = str
    body['label'] = label
    link(id, body)


# 将图片转换成base64
def base(file):
    f = open(file, 'rb')
    byteC = base64.b64encode(f.read())
    # 将base64解码成字符串
    f.close()
    return byteC.decode('utf-8')


def txt(path):
    a = []
    for line in open(path, 'r', encoding='UTF-8'):
        # print(line),
        a.append(line)
    return a


a = txt(r"D:\工作\data1400.txt")
list_json = os.listdir(img_paths)
for i in list_json:
    img_json(img_paths + i, a)
