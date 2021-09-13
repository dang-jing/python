# -*- coding:utf-8 -*-

import pandas as pd
import json
import os
#   读取excel，生成json文件

#   json写入文件夹路径
kgpath = 'D:\\b\\11\\'

df = pd.read_excel(r'D:\b\知识图谱(1).xlsx', sheet_name='代数知识图谱', keep_default_na=False)
kgURI = df.get('id')
kgname = df.get('中文命名')
kgContent = df.get('内容')
relations = df.get('关系描述')


def app(con, aa, uu):
    if '0' == uu:
        uu = ''
    else:
        uu = uu
    return con.append({
        'title': aa,
        "description": uu
    })


def set(con, name):
    i = len(con)
    if 'similar' == name:
        if i < 5:
            for i in range(5 - i):
                con.append({
                    'title': '',
                    "description": ''
                })
    else:
        if i < 3:
            for i in range(3 - i):
                con.append({
                    'title': '',
                    "description": ''
                })


def set_json(kg, name):
    #   json_str = json.dumps(kg, ensure_ascii=False)
    #   print(json_str)

    if not os.path.exists(kgpath[:1]):
        os.makedirs(kgpath[:1])
    with open(kgpath + name + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(kg, json_file)


def start():
    for i in range(len(kgname)):
        kg = dict()
        name = kgname[i]
        kg['kgName'] = name
        kg['kgURI'] = kgURI[i]
        kg['kgContent'] = kgContent[i]
        kg['backgroundKG'] = [
            {
                "name": "概念或规则引入的背景介绍，可以是小故事",
                "content": "内容"
            },
            {
                "name": "在实际生活中的应用或者意义",
                "content": "内容"
            },
            {
                "name": "发展历史",
                "content": "内容"
            }
        ]
        kg['explainContent'] = [{'title': '', 'content': '', '$ref': ''}, {'title': '', 'content': '', '$ref': ''}]
        kg['explainVideoURL'] = ''
        kg['learnDifficultyLever'] = ''
        kg['kgLabel'] = [
            "数学概念",
            "几何概念"
        ]
        kg['practiseCase'] = {'easy': ['', ''], 'normal': ['', ''], "hard": ['', '']}
        yy = str(relations[i]).split('\n')

        rel = dict()
        Inclusion, Reason, Hierarchy, MathLogic, Aggregation, Elaboration = [], [], [], [], [], []
        for j in yy:
            i_split = j.split(',')
            print(j)
            if '1' == i_split[0]:
                app(Inclusion, i_split[1], i_split[2])
            elif '2' == i_split[0]:
                app(Reason, i_split[1], i_split[2])
            elif '3' == i_split[0]:
                app(Hierarchy, i_split[1], i_split[2])
            elif '4' == i_split[0]:
                app(MathLogic, i_split[1], i_split[2])
            elif '5' == i_split[0]:
                app(Aggregation, i_split[1], i_split[2])
            elif '6' == i_split[0]:
                app(Elaboration, i_split[1], i_split[2])
        set(Inclusion, 'Inclusion')
        set(Reason, 'Reason')
        set(Hierarchy, 'Hierarchy')
        set(MathLogic, 'MathLogic')
        set(Aggregation, 'Aggregation')
        set(Elaboration, 'Elaboration')
        rel['Inclusion'] = Inclusion
        rel['Reason'] = Reason
        rel['Hierarchy'] = Hierarchy
        rel['MathLogic'] = MathLogic
        rel['Aggregation'] = Aggregation
        rel['Elaboration'] = Elaboration
        kg['relations'] = rel
        set_json(kg, name)


if __name__ == '__main__':
    start()

    '''kg['parentNodes'] = [{'name': '', '$ref': ''}, {'name': '', '$ref': ''}]
    kg['childNodes'] = [{'name': '', '$ref': ''}, {'name': '', '$ref': ''}]
    kg['brotherNodes'] = [{'name': '', '$ref': ''}, {'name': '', '$ref': ''}]
    kg['relationCase'] = [{'level1': ['', '']}, {'level2': ['', '']}]'''
