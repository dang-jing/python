# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch
import json
import os
import uuid

img_paths = 'D:\\图片\\拍照解题\\json\\'


def link(id, body):
    es = Elasticsearch(['192.168.3.10:9200'])
    print(es.index(index='label_data', doc_type='doc', id=id, body=body))


def get_json(json_name):
    jsonx = dict()
    with open(img_paths + json_name, 'r', encoding='utf-8') as path_json:  # gb18030
        jsonx = json.load(path_json)
    return jsonx


def img_json():
    body = dict()
    body['question_types'] = '解答题'
    body['subject_quality'] = '仅题目相关'
    body['topic_hierarchy'] = '单题目'
    body['is_answer'] = '无答案'
    body['picture_type'] = '标准截图'
    body['picture_quality'] = '合格'
    return  body


listdir = os.listdir(img_paths)
for i in listdir:
    body = img_json()
    json1 = get_json(i)
    body['label'] = json1
    uuid_ = uuid.uuid1()
    link(uuid_, body)
