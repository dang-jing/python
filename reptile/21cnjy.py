# -*-coding:utf-8-*-
import urllib

import requests
from lxml import etree
import os
import uuid
import time
import json
from PIL import Image

URL = 'https://www.21cnjy.com/3/20152_7/'
file_path = 'C:\\Users\\dangc\\Desktop\\a\\111\\'
txtPath = r'D:\测试\中考\21cnjy.txt'
json_path = 'C:\\Users\\dangc\\Desktop\\a\\111\\'
start, finish = 1, 2
province = ['内蒙古', '北京', '天津', '上海', '重庆', '广西', '宁夏', '新疆', '西藏', '香港', '澳门', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏',
            '浙江', '安徽', '福建', '江西', '山东', '台湾', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海']
pp = []

class TwoOnecnjy():

    def __init__(self):
        # self.set_json('北京市首都师范大学附属中学教育集团2020-2021学年第一学期七年级上册数学期末考试卷（PDF版含答案）')
        self.parsing()
        # self.img_webPage('https://www.21cnjy.com/H/3/48901/8687188.shtml')

    def parsing(self):
        label = self.url(URL)
        webPage = label.xpath('//div[@class="pages-items"]//a//@href')
        self.hrefs = webPage[0][:-1]
        for i in range(start, finish):
            a = '{}{}{}'.format('https://www.21cnjy.com', self.hrefs, i)
            print(a, '-----------------------------------现在是第', i, "页---d到", finish , '页结束')
            label = self.url(a)
            # 获取所有的word的url
            hrefs = label.xpath('//div[@class="item-mc"]//p//a//@href')
            titles = label.xpath('//div[@class="item-mc"]//p//a//@title')
            if len(hrefs) >3 :
                '''print(hrefs)
                print(titles)'''
                for i in range(2, len(hrefs)):
                    print(titles[i], hrefs[i], "----------------", i + 1, '/', len(titles))

                    self.set_json(titles[i])
                    self.img_webPage(hrefs[i])
            else:
                print("没有试题可以爬了")
                break

    # 对json文件写入数据
    def set(self):
        # a = {'imageData': 'aaaaaa'}
        # 判断路径是否存在，如果没有这个path则直接创建
        if not os.path.exists(json_path[:-1]):
            os.makedirs(json_path[:-1])
        json_str = json.dumps(self.json, ensure_ascii=False)
        img_name = '{}{}'.format(self.img_name, '.json')
        with open(json_path + img_name, 'w', encoding='utf-8') as json_file:
            json_file.write(json_str)

    # 解析图片网页 https://www.21cnjy.com/H/3/48901/9290987.shtml
    def img_webPage(self, href):
        #self.json = dict()
        label = self.url(href)
        img_urls = label.xpath('//div[@class="win-viewer-files f-usn"]//img/@src')
        if 0 != len(img_urls):
            # print(img_urls)
            size = len(img_urls)
            for i in range(size):
                img_url = img_urls[i]
                self.json['page'] = '{}{}{}'.format(i + 1, "/", size)
                self.json['download_url'] = img_url
                # 判断源码是否已存在
                if self.findURL(img_url):
                    self.url_picture(img_url)
                    self.set()
                else:
                    continue
        else:
            print(href, '没有图片')

    # 将浏览器图片下载到指定路径下
    def url_picture(self, image_url):
        # 判断路径是否存在，如果没有这个path则直接创建
        if not os.path.exists(file_path[:-1]):
            os.makedirs(file_path[:-1])
        file_suffix = uuid.uuid1()
        self.img_name = file_suffix
        file_name = '{}{}'.format(file_suffix, '.png')
        # 拼接字符串
        filename = '{}{}'.format(file_path, file_name)
        # 根据url将图片下载到本地
        urllib.request.urlretrieve(image_url, filename=filename)
        print(filename, "下载完成")
        self.json['file_name'] = file_name
        self.json['date_captured'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.json['save_path'] = filename
        self.getPhysicalSize(filename)
        f2 = open(txtPath, 'a')
        f2.write(image_url + '\n')

    # 在文本文件中看是否有该url地址，有的话返回true
    def findURL(self, img_url):
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

    def getPhysicalSize(self, fn):
        # 打开图像文件并获取以像素为单位的尺寸
        im = Image.open(fn)
        # print(im)
        self.json['width'], self.json['height'] = im.size

    def set_json(self, title):
        self.json = dict()
        self.json['title'] = title
        self.json['subject'] = '数学'
        title = title.split('（')[0]
        # print(title)
        if '学年' in title:
            self.json['papers_year'] = title.split('学年')[0][-9:]
        elif '年' in title:
            self.json['papers_year'] = title.split('年')[0][-9:]
        region = []
        if '省' in title:
            region = title.split('省')
            self.json['region'] = region[0][-2:]
        else:
            for i in province:
                if i in title:
                    try:
                        cc = title.split(i[0])[0][-1]
                        print(cc)
                        region = ['0', title.split(cc)[1]]
                        break
                    except IndexError:
                        region = ['0', title]
                        break
        # print(region)
        if len(region) != 0:
            sisson = []
            if '县' in region[1]:
                sisson = region[1].split('县')
                self.json['sisson'] = sisson[0] + '县'
            elif '区' in region[1]:
                sisson = region[1].split('区')
                self.json['sisson'] = sisson[0] + '区'
            elif '市' in region[1]:
                sisson = region[1].split('市')
                self.json['sisson'] = sisson[0] + '市'
            if len(sisson) != 0:
                if '中学' in sisson[1]:
                    self.json['school'] = sisson[1].split('中学')[0] + '中学'
        self.json['subject'] = '数学'
        self.json['class'] = '初中'
        if '复习' in title:
            self.json['papers_type'] = '练习题'
        elif '期末' in title:
            self.json['papers_type'] = '期末试卷'
        grade = ''
        if '七年级' in title:
            grade = '七年级'
        elif '八年级' in title:
            grade = '八年级'
        elif '九年级' in title:
            grade = '九年级'
        if '学期' in title:
            a = title.split('学期')[0]
            if '上' in a[-1] or '下' in a[-1]:
                self.json['grade'] = grade + a[-1] + '学期'
            else:
                self.json['grade'] = grade + a[-2:] + '学期'
        if '复习' in title:
            if '：' in title:
                self.json['knowledge'] = title.split('：')[1]
            else:
                self.json['knowledge'] = title.split('复习')[1]
                # label = self.json
        # print(label)

    # 请求页面
    def url(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        # 获取网页信息，verify关闭ssl校验
        response = requests.get(url=url, headers=headers, verify=False)
        # print(response.text)
        # 设置读取网页编码级
        # response.encoding = 'utf-8'
        # 拿到页面内容
        response = response.content
        # 页面内容转为xpath可解析内容
        label = etree.HTML(response)
        return label


TwoOnecnjy()
