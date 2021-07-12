# -*- coding:utf-8 -*-

from PIL import Image as ImagePIL, ImageFont, ImageDraw
import glob
import os

try:
    from PIL import Image
except ImportError:
    import Image

def test():
    im = ImagePIL.open(r"D:\图片\分类\不常规照\f1197396b91e466ba523fa3f20ffc207.jpg")
    im.save(r'D:\图片\分类\2.jpg',dpi=(2000.0,2000.0))

def thumbnail():
    img_path = glob.glob(r"D:\图片\分类\11\*.jpg")
    print(img_path)
    path_save = r'D:\图片\分类\\'
    for file in img_path:
        print(file)
        name = os.path.join(path_save, file)
        im = Image.open(file)
        im.thumbnail((1920,1280))
        print(im.format, im.size, im.mode)
        im.save(name,'JPEG')

if __name__ == '__main__':
    thumbnail()