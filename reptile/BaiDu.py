# -*-coding:utf-8-*-


import requests
import json
import time
import uuid
import os
import urllib.request
from faker import Factory
import random
import re

a = "二元一次方程组"
start_a, finish = 1, 10


def start(query, begin, end):
    # 记录爬取图片源地址的文本
    txtPath = "D:\\图片\\测试.txt"
    # 本地下载图片地址
    urlPath = "D:\\测试\\中考\\imgs\\二元一次方程组\\"
    total = 0
    for i in range(begin, end + 1):

        print("第", i, "页-----------------------还剩", end - i)
        j = i*30
        page = dec2hex(j)
        url = "http://image.baidu.com/search/acjson?tn=resultjson_com&logid=6650215631444446200&ipn=rj&ct=201326592" \
              "&is=&fp=result&queryWord=" + query + "&cl=2&lm=-1" \
                                                    "&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=" \
                                                    "&word=" + query + "&s=&se=&tab=&width=&height=" \
                                                                       "&face=&istype=&qc=&nc=1&fr=&expermode=&nojc=&pn="+str(j)+"&rn=30&gsm=" + page + "&1626508879965="
        print(url)
        urlPaths = parsing_URL(url)
        # print(urlPaths)
        for i in urlPaths:
            if findURL(i, open(txtPath)):
                continue
            url_picture(i, urlPath)
            f2 = open(txtPath, 'a')
            f2.write(i + '\n')
            total += 1
        # 程序等待两秒
        time.sleep(2)
    print("总共爬取", total, "张图片")


# 十进制转为十六进制
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])


# 解析网页返回内容，拿到指定键的所有内容
def parsing_URL(url):
    # 设置请求头，默认为python，防止被拦截
    random.randint(0, 2) + random.random()
    #   随机更改请求头
    fc = Factory.create()
    headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
        # "User-Agent": fc.user_agent()
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': fc.user_agent(),
        'Upgrade-Insecure-Requests': '1'
    }
    # 获取网页信息，verify关闭ssl校验
    response = requests.get(url=url, headers=headers, verify=False)
    # 拿到请求页面发布会的所有内容
    jsonobj = json.loads(response.text)
    imgPaths = jsonobj['data']
    # print(imgPaths)
    imgList = []
    a = 0
    # 拿到所有的图片源地址放入集合中
    for imgPath in imgPaths:
        # print(imgPath)
        if imgPath == {}:
            break
        imgList.append(imgPath['thumbURL'])
        a += 1
    return imgList


# 在文本文件中看是否有该url地址，有的话返回true
def findURL(url, txtPath):
    a = url + '\n'
    finder = False
    while True:
        # 单行读取文件内容
        str = txtPath.readline()
        if str == a:
            print(a[0:-1], "-----------已存在")
            finder = True
            break
        # readline读取到最后没数据时返回为空
        # 读取文件内容为空时，跳出循环体
        elif str == '':
            break
    return finder


# 将浏览器图片下载到指定路径下
def url_picture(image_url, file_path):
    # image_url = 'https://gss0.baidu.com/7Po3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=48bb1719d433c895a62b907de1235fc8/b2de9c82d158ccbf2b1ed5b414d8bc3eb0354199.jpg'
    # file_path = 'D:\\图片\\测试\\'
    # file_name = image_url
    try:
        # 判断路径是否存在，如果没有这个path则直接创建
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_suffix = uuid.uuid1()
        # 拼接字符串
        filename = '{}{}{}'.format(file_path, file_suffix, '.jpg')
        # 根据url将图片下载到本地
        urllib.request.urlretrieve(image_url, filename=filename)
        print(filename, "下载完成")
    except IOError as e:
        print(1, e)
    except Exception as e:
        print(2, e)


start(a, start_a, finish)
'''if __name__ == '__main__':
    fc = Factory.create()
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': fc.user_agent(),
        'Upgrade-Insecure-Requests': '1'
    }

    A = requests.Session()
    A.headers = headers
    Result = A.get(
        'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7254038348844683383&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E4%BA%8C%E5%85%83%E4%B8%80%E6%AC%A1%E6%96%B9%E7%A8%8B%E7%BB%84&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E4%BA%8C%E5%85%83%E4%B8%80%E6%AC%A1%E6%96%B9%E7%A8%8B%E7%BB%84&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&nojc=&rn=30&gsm=1e&1626509680746=',
        timeout=7, allow_redirects=False)
    result = Result.text
    pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
    print(Result.text)
    print(Result.headers)'''
