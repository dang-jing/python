import base64
import io
import re
import json

try:
    from PIL import Image
except ImportError:
    import Image


def deal_inspect_img(base64_str):
    '''"""裁剪base64字符串的图片"""
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)'''
    byte_data = base64.b64decode(base64_str)
    # BytesIO 对象

    image_data = io.BytesIO(byte_data)
    print(type(image_data))
    # 得到Image对象
    img = Image.open(image_data)
    # 裁剪图片(左，上，右，下)，笛卡尔坐标系
    img2 = img.crop((17, 0, 621, 54))

    # BytesIO 对象
    imgByteArr = io.BytesIO()
    # 写入BytesIO对象
    img2.save(imgByteArr, format='png')
    # 获得字节
    imgByteArr = imgByteArr.getvalue()
    base64_str = base64.b64encode(imgByteArr)
    return base64_str


if __name__ == '__main__':
    jsonx = dict()
    with open(r'C:\Users\dangc\Pictures\2选择\屏幕截图 2021-04-20 101752.json', 'r',
              encoding='utf-8') as path_json:  # gb18030
        jsonx = json.load(path_json)
    imgdata = jsonx['imageData']
    str11 = imgdata
    base64_str = deal_inspect_img(str11)
    imgdata = base64.b64decode(base64_str)
    with open('111.jpg', 'wb') as f:
        f.write(imgdata)
