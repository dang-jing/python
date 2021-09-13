# -*- coding:utf-8 -*-
#   生成uri

import configparser
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(BASE_DIR, "id.conf")
cf = configparser.ConfigParser()
# os.path.join 以适应linux和windows不同目录分隔符的写法
cf.read(path)


def geometry(topic, name, type):
    if '几何' == topic:
        topic = 'geometry'
        ss = 'axskg:math/geometry/'
        ob = '00010010'
    elif '代数' == topic:
        topic = 'algebra'
        ss = 'axskg:math/geometry/'
        ob = '00010001'
    else:
        ss = ''
        topic = ''
        ob = ''
    if '定义' == type:
        ss = number(ss, topic, 'concepts', ob+'00000001', name, type)
    elif '定理' == type:
        ss = number(ss, topic, 'rules', ob+'00000100', name, type)
    elif '关系' == type:
        ss = number(ss, topic, 'relations', ob+'00000010', name, type)
    else:
        ss = number(ss, topic, 'rules', ob+'00000100', name, type)
    return ss


def number(ss, topic, type, ob, name, a):
    ss = ss + type + '/' + name
    concepts = cf.getint(topic, type)
    con = bin(concepts)[2:]
    len1 = len(con)
    eee = ''
    for i in range(16 - len1): eee += '0'
    if '内部实现' == a:
        l = list(ob)
        l[11] = '1'
        ob = ''.join(l)
        print(name+':内部实现')
    len1 = eee + con
    len1 = int(ob + len1, 2)
    ss = ss + '#' + str(len1)
    cf.set(topic, type, str(concepts + 1))
    with open(path, "w+") as f:
        cf.write(f)
    return ss


#   教材uri
def teaching(name):
    if '人教版' == name:
        s = '0001100000000001'
        return joint('teaching', 'taught', name, s)


def joint(topic, type, name, ob):
    ss = 'axskg:math/' + name
    #   读取配置文件[topic]下的type
    concepts = cf.getint(topic, type)
    con = bin(concepts)[2:]
    len1 = len(con)
    eee = ''
    for i in range(16 - len1): eee += '0'
    len1 = eee + con
    len1 = int(ob + len1, 2)
    ss = ss + '#' + str(len1)
    cf.set("teaching", type, str(concepts + 1))
    with open("id.conf", "w+") as f:
        cf.write(f)
    return ss


if __name__ == '__main__':
    # print(geometry('几何', '线段包含', '内部实现', '定理'))
    print(teaching('北师大版'))
    # start()

'''#   获取所有section 就是[]
secs = cf.sections()
#   获取section对应下的所有的key
opts = cf.options("db")
#   获取section对应下的所有的key，values
kvs = cf.items("db")
print(secs)'''
'''cf.read("id.conf", encoding="utf-8")
cf.set("geometry", "concepts", '5')
with open("id.conf", "w+") as f:
    cf.write(f)'''
