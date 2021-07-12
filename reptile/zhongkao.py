# -*_coding:utf8-*-

import requests
from lxml import etree
import os
import uuid
import urllib.request
import time
import json
from PIL import Image


# 爬取页码
page1, page2 = 1, 2
# 爬取路径
URL = "http://www.zhongkao.com/zyk/zkzt/sxzt/index.shtml"

# 图片存储路径
img_path = r"D:\测试\中考\imgs"
#   图片对应json存放位置
json_path = r"D:\测试\中考\img_json"
#   记录爬取的图片源地址
txtPath = r'D:\测试\中考\img_path.txt'
province = ['内蒙古', '北京', '天津', '上海', '重庆', '广西', '宁夏', '新疆', '西藏', '香港', '澳门', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏',
            '浙江', '安徽', '福建', '江西', '山东', '台湾', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海']


def start():
    for j in range(page1, page2):
        if j == 1:
            txts, hrefs = zhongkao_URL(URL)
            for i in range(len(txts)):
                print(txts[i], hrefs[i], "----------------", i + 1, '/', len(txts) + 1)
                paper_url(txts[i], hrefs[i])
        else:
            print(j)
            txts, hrefs = zhongkao_URL('{}{}{}{}'.format(URL.split('index')[0], 'index_', j, '.shtml'))
            for i in range(len(txts)):
                print(txts[i], hrefs[i], "----------------", i + 1, '/', len(txts) + 1)
                paper_url(txts[i], hrefs[i])


def getPhysicalSize(fn):
    # 打开图像文件并获取以像素为单位的尺寸
    im = Image.open(fn)
    # print(im)
    width, height = im.size
    return width, height


def pag(txt):
    a = ['图片', '已公布', '已上线']
    b = False
    for i in a:
        if i in txt and '考' in txt:
            b = True
    #print(b)
    return b


# 处理试卷页面
def paper_url(txt, paperurl):
    # print(txt)
    if pag(txt):
        img_json = dict()
        txt_json(txt, img_json)
        label = url(paperurl)
        img_url = label.xpath('//div[@class="content ft14"]//img/@src')
        img_json['page'] = 1
        # 判断是否有答案
        if img_json['is_answer'] == 'true':
            folder_name = "\\answer\\"
            file = url_picture(img_url[1], img_path + folder_name, img_json)
            folder = json_path + folder_name
            path = '{}{}{}'.format(folder, file, '.json')
            set(img_json, path, folder)
        else:
            folder_name = "\\no_answer\\"
            file = url_picture(img_url[1], img_path + folder_name, img_json)
            folder = json_path + folder_name
            path = '{}{}{}'.format(folder, file, '.json')
            set(img_json, path, folder)
        pages_url = label.xpath('//div[@class="pages"]//a/@href')
        print(pages_url)
        for i in range(len(pages_url) - 1):
            img_json = dict()
            txt_json(txt, img_json)
            img_json['page'] = '{}{}{}'.format(i + 2, '/', len(pages_url))
            a = pages_url[i]
            img_url = url(a)
            # print(len(pages_url))
            if findURL(img_url[1]):
                img_url = img_url.xpath('//div[@class="content ft14"]//img/@src')
                #print(img_url)
                if len(img_url) > 1:
                    if img_json['is_answer'] == 'true':
                        folder_name = "\\answer\\"
                        file = url_picture(img_url[1], img_path + folder_name, img_json)
                        folder = json_path + folder_name
                        path = '{}{}{}'.format(folder, file, '.json')
                        set(img_json, path, folder)
                    else:
                        folder_name = "\\no_answer\\"
                        file = url_picture(img_url[1], img_path + folder_name, img_json)
                        folder = json_path + folder_name
                        path = '{}{}{}'.format(folder, file, '.json')
                        set(img_json, path, folder)


# 对字符串进行处理，写入json
def txt_json(txt, img_json):
    txt = txt.split('（')[0]
    img_json['title'] = txt
    if '年' in txt:
        a = txt.split('年')
        img_json['papers_year'] = a[0]
    else:
        e = txt[:4]
        img_json['papers_year'] = e
        a = txt.split(txt[3])
    if '中考' in a[1]:
        b = a[1].split('中考')
    elif '考' in a[1]:
        b = a[1].split('考')
    if '省' not in b[0]:
        str = isprovince(b[0])
        img_json['region'] = str
        img_json['sisson'] = b[0][len(str):]
    else:
        e = b[0].split('省')
        img_json['region'] = e[0]
        img_json['sisson'] = e[1]
    if '答案' in b[1]:
        img_json['is_answer'] = 'true'
    else:
        img_json['is_answer'] = 'false'
    img_json['subject'] = b[1][:2]
    img_json['papers_type'] = b[1][2:4]
    img_json['class'] = '初中'
    # return img_json


def isprovince(str):
    for i in province:
        if i in str:
            str = i
            break
    return str


# 对json文件写入数据
def set(json_data, file, folder):
    # a = {'imageData': 'aaaaaa'}
    # 判断路径是否存在，如果没有这个path则直接创建
    if not os.path.exists(folder):
        os.makedirs(folder)
    json_str = json.dumps(json_data, ensure_ascii=False)
    with open(file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)


# 将浏览器图片下载到指定路径下
def url_picture(image_url, file_path, img_json):
    # 判断源码是否已存在
    if findURL(image_url):
        # 判断路径是否存在，如果没有这个path则直接创建
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_suffix = uuid.uuid1()
        file_name = '{}{}'.format(file_suffix, '.png')
        # 拼接字符串
        filename = '{}{}'.format(file_path, file_name)
        # 根据url将图片下载到本地
        urllib.request.urlretrieve(image_url, filename=filename)
        print(filename, "下载完成")
        img_json['download_url'] = image_url
        img_json['file_name'] = file_name
        img_json['date_captured'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        img_json['save_path'] = filename
        width, height = getPhysicalSize(filename)
        img_json['width'] = width
        img_json['height'] = height
        f2 = open(txtPath, 'a')
        f2.write(image_url + '\n')
        return file_suffix


# 在文本文件中看是否有该url地址，有的话返回true
def findURL(img_url):
    Path = open(txtPath)
    a = '{}{}'.format(img_url, '\n')
    finder = True
    # print('来了',img_url)
    for line in Path:
        # 单行读取文件内容
        # str = Path.readline()
        # print(line,a)
        if line == a:
            print(a[0:-1], "-----------已存在")
            finder = False
            break
        # readline读取到最后没数据时返回为空
        # 读取文件内容为空时，跳出循环体
        elif str == '':
            break
    # print(finder)
    return finder


# 请求页面
def url(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    # 获取网页信息，verify关闭ssl校验
    response = requests.get(url=URL, headers=headers, verify=False)
    # print(response.text)
    # 设置读取网页编码级
    # response.encoding = 'utf-8'
    # 拿到页面内容
    response = response.content
    # 页面内容转为xpath可解析内容
    label = etree.HTML(response)
    return label


# 处理首页
def zhongkao_URL(URL):
    print(URL)
    label = url(URL)
    # print(type(label))
    # 拿到标签h3class为ft16 bm5，下的a的text文本/href属性
    txts = label.xpath('//h3[@class="ft16 bm5"]//a/text()')
    hrefs = label.xpath('//h3[@class="ft16 bm5"]//a/@href')
    print(txts, hrefs)
    return txts, hrefs


if __name__ == '__main__':
    #paper_url('2018年各地中考数学试卷精选汇编概率五答案（图片版）','http://www.zhongkao.com/e/20190224/5c71f10664efe.shtml')
    start()
    # 页码过长手动爬取
    '''txts=['2019年湖北鄂州中考数学真题（已公布）', '2019年湖北鄂州中考数学真题（图片版）', '2019年山东烟台中考数学真题答案（已公布）']
    href=['http://www.zhongkao.com/e/20190629/5d1737796c26b.shtml', 'http://www.zhongkao.com/e/20190629/5d17376746312.shtml', 'http://www.zhongkao.com/e/20190629/5d17363b2ded3.shtml']
    for i in range(len(txts)):
        print(i)
        paper_url(txts[i],href[i])'''
    '''a = '2020年内蒙古呼和浩特中考数学真题答案（图片版）'
    b = 'http://www.zhongkao.com/e/20210108/5ff812410e3c9.shtml'
    paper_url(a, b)'''
    '''a = [1, 2, 3]
    i = 1
    b = '{}{}{}'.format(i + 2, '/', len(a))
    print(b)'''
    '''str = "2020年内蒙古呼和浩特中考数学真题答案（图片版）"
    a = dict()
    txt_json(str, a)
    print(a)'''
    # start()
