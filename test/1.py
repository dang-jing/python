# -*_coding:utf8-*-
import json
import base64

def a():
    #读取json格式文件数据
    with open(r'C:\Users\dangc\Pictures\模块2标注json\0.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        #拿到指定键对应的值
        print(type(json_data))
        img = json_data['imageData']
        print(img)
        #读取base64图片数据编码格式数据
        img = base64.b64decode(img)
        fh=open(r"C:\Users\dangc\Pictures\模块2标注json\1.jpg",'wb')
        fh.write(img)
        fh.close()

if __name__ == '__main__':
    txts=['2019年湖北鄂州中考数学真题（已公布）', '2019年湖北鄂州中考数学真题（图片版）', '2019年山东烟台中考数学真题答案（已公布）']
    print(str[3])


