# -*-coding:utf-8-*-


import requests
import json
import time
import uuid
import os
import urllib.request

a = "初三数学题"
start_a, finish = 1, 500


def start(query, begin, end):
    # 记录爬取图片源地址的文本
    txtPath = "D:\\图片\\测试.txt"
    # 本地下载图片地址
    urlPath = "D:\\图片\\手写\\初三数学题\\"
    total = 0
    for i in range(begin, end + 1):
        print("第", i, "页-----------------------还剩", end - i)
        page = dec2hex(i)
        url = "https://m.baidu.com/sf/vsearch/image/search/wisesearchresult?tn=wisejsonala&ie=utf-8&fromsf=1" \
              "&word="+query+"&pn=30&rn=30&gsm=&prefresh=undefined&fp=result&searchtype=0&fromfilter=0&tpltype=0"
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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    # 获取网页信息，verify关闭ssl校验
    response = requests.get(url=url, headers=headers, verify=False)
    # 拿到请求页面发布会的所有内容
    jsonobj = json.loads(response.text)
    imgPaths = jsonobj['linkData']
    # print(imgPaths)
    imgList = []
    a = 0
    # 拿到所有的图片源地址放入集合中
    for imgPath in imgPaths:
        # print(imgPath)
        if imgPath == {}:
            break
        imgList.append(imgPath['hoverUrl'])
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
