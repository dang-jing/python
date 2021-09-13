import pandas as pd
from kit.URLid import generate_id

#   读取excel获取教材分布，生成人教版数据uri

path = r'D:\b\1.json'


def start():
    #                                               读取指定子列表                 将为nan的值返回为''
    df = pd.read_excel(r'D:\b\三角形知识图谱 .xlsx', sheet_name='三角形知识图谱', keep_default_na=False)
    name = df['id']
    lll = df['教材分布']
    js = dict()
    jsons = dict()
    nodes = []
    links = []
    for i in range(len(lll)):
        i_ = lll[i]
        if '' != i_ and '小学' != i_:
            #st(name[i],i_ , js,nodes, links)
            print(i_)
        else:
            print('111' + i_)
    jsons['nodes'] = nodes
    jsons['links'] = links
    '''json_str = json.dumps(jsons, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)'''


def st(id, ss, js, nodes, links):
    split = ss.split('|')
    for i in range(len(split)):
        json = dict()
        name = split[i]
        if '人教版' == name:
            if '人教版' in js.keys():
                continue
            else:
                js[name] = generate_id.teaching('人教')
                jj(id, json, False, 'tree', True)
        else:
            to_json = dict()
            if name not in js.keys():
                js[name] = generate_id.teaching('人教')
            jj(id, json, False, 'tree', False)
            to_json['from'] = js[split[i - 1]]
            to_json['to'] = split[name]
            to_json['text'] = '组合关系'
            links.append(to_json)
        nodes.append(json)


def jj(id, json, courseware, shape, headNode):
    name_id = id.split('/')[-1].split('#')
    json['id'] = name_id[1]
    json['name'] = name_id[0]
    attribute = dict()
    attribute['courseware'] = courseware
    attribute['highlight'] = 'true'
    attribute['shape'] = shape
    attribute['uri'] = id
    attribute['headNode'] = headNode


start()
