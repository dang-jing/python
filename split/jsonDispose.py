# -*_coding:utf8-*-
import json
import math
import cv2
import numpy as np
import base64

# 读取json地址
jsonPath = r"C:\Users\dangc\Pictures\2选择\屏幕截图 2021-04-20 101752.json"
# 写入子json地址
sonjsonpath = r'D:\工作\屏幕截图 2021-04-20 101752-1.json'
#  需要截取的table
value = '1'
# jsons = os.listdir(jsonPath)
dir_txt = r'D:\python\demo\split\txt\1.jpg.txt'
imgpath = r"C:\Users\dangc\Pictures\2选择\屏幕截图 2021-04-20 101752.png"
# 截取图片存放地址
splitimg = r".\\result\\1.jpg"


# 读取json文件
def get():
    with open(jsonPath, 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        jsonData = json_data['shapes']
        json_data.pop('imageData')
        print(jsonData)
        shapes = []
        points = []
        # 拿到要截图目标的图片地址
        for i in jsonData:
            print(value)
            label = i['label']
            if label == value:
                points = i['points']
                # json2txt(points)
            # print(label)
        x = int(points[0][0])
        y = int(points[0][1])
        x1 = int(points[1][0])
        y1 = int(points[1][1])
        print(y, y1, x, x1)
        split(y, y1, x, x1)
        json_data['imageData'] = base(splitimg)
        print(json_data['imageData'])
        for i in jsonData:
            xy = i['points']
            if i['label'] != value:
                a = xy[0][0]
                b = xy[0][1]
                print(a, b)
                # 判断标注是否在截取地址内，只拿在地址内的所有标注
                if x < a and a < x1 and y < b and b < y1:

                    print(xy)
                    shapes.append(i)
        print(shapes)
        json_data.pop('shapes')

        json_data['shapes'] = shapes
        # print(json_data)
        return json_data


# 将json中xy两点坐标计算出四点坐标放入文本中
def json2txt(xy):
    i = 0
    with open(dir_txt, 'w', encoding='utf-8') as ftxt:
        strxy = ''
        for m, n in xy:
            if i == 0:
                strxy += str(int(m)) + ',' + str(int(n)) + ','
                strxy += str(math.ceil(xy[1][0])) + ','
                strxy += str(int(n)) + ','
                i = i + 1
            else:
                strxy += str(math.ceil(m)) + ',' + str(math.ceil(n)) + ','
                strxy += str(int(xy[0][0])) + ','
                strxy += str(math.ceil(n)) + ','
        i = 0
        ftxt.writelines(strxy + "\n")


def split(y, y1, x, x1):
    img = cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    ROI = img[y:y1, x:x1]
    if ROI.size != 0:
        str = splitimg
        cv2.imencode('.jpg', ROI)[1].tofile(splitimg)
        return str
    return ''


# 对json文件写入数据
def set(json_data):
    # a = {'imageData': 'aaaaaa'}
    file = sonjsonpath
    f_obj = open(file, 'w')
    json_str = json.dumps(json_data)
    with open(file, 'w') as json_file:
        json_file.write(json_str)
    f_obj.close()

#将图片转换成base64
def base(file):
    f=open(file,'rb')
    byteC = base64.b64encode(f.read())
    #将base64解码成字符串
    return byteC.decode('utf-8')


if __name__ == '__main__':
    get = get()
    print(get)
    set(get)
    # print(base(r"D:\python\demo\split\result\1.jpg")[2:-1])
    #print(base(r"D:\python\demo\split\result\1.jpg"))
'''img = base64.b64decode(img)
        fh=open("C:\\Users\\dangc\\Pictures\\模块2标注json\\1.jpg",'wb')
        fh.write(img)
        fh.close()'''
