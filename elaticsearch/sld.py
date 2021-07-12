# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
import base64
import uuid
import os
import json

img_paths = r'D:\图片\拍照解题\json'


def link(id, body):
    es = Elasticsearch(['192.168.3.10:9200'])
    print(es.index(index='dataset', doc_type='doc', id=id, body=body))
    # print(es.get(index='py2', doc_type='doc', id=1))


def img_json(label_json):
    shapes = label_json.pop('shapes')
    list = []
    body = dict()
    print(label_json)
    for i in shapes:
        if 'topic' in i['label']:
            a = i['label'].split('|')
            body['question_types'] = a[1]
            body['topic _type'] = a[2]
            body['subject_quality'] = a[3]
            body['topic_hierarchy'] = a[4]
            body['txt_graph'] = a[5]
            body['is_answer'] = a[6]
            body['picture_type'] = a[7]
            body['picture_quality'] = a[8]
        list.append(i)
    print(list)
    label_json['shapes'] = list
    id = uuid.uuid1()
    label_json['imagePath'] = id
    body['label'] = label_json
    link(id,body)


def read_json(path_json):
    with open(path_json, 'r', encoding='utf-8') as path_json:  # gb18030
        jsonx = json.load(path_json)
    return jsonx


if __name__ == '__main__':
    a = read_json(img_paths + '\\image1.json')
    img_json(a)
# 拿到文件夹所有文件名+
'''list_json = os.listdir(img_paths)
print(list_json)
for i in list_json:
    label_json = read_json(img_paths + i)
    img_json(label_json)'''
