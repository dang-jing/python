# -*_coding:utf8-*-

import os
from PIL import Image

#   切分图片地址
img_path = 'C:\\Users\\dangc\\Desktop\\a\\111\\'
#   生成图片地址
split_path = 'C:\\Users\\dangc\\Desktop\\a\\'
#   切分数
count = 3
type = '.png'
#   百分比切框，不切输入none,上下，左右
percent_1, percent_2 = 0.0816, 0.0962
#percent_1, percent_2 = None, None


def start():
    listdir = os.listdir(img_path)
    for i in listdir:
        name = i.split('.')
        if type[1:] == name[1]:
            img(name[0])


def img(name):
    image_open = Image.open(img_path + name + type)
    if percent_1:
        w, h = image_open.size
        a = int((w * percent_2) / 2)
        b = int((h * percent_1) / 2)
        image_open = image_open.crop((a, b, w - a, h - b))
    w, h = image_open.size
    a = h / count
    box_list = []
    for i in range(count):
        box = (0, i * a, w, (i + 1) * a)
        box_list.append(box)
    image_list = [image_open.crop(box) for box in box_list]
    save_images(name, image_list)


# 保存分割后的图片
def save_images(name, image_list):
    index = 1
    for image in image_list:
        image.save(split_path + name + '_' + str(index) + type)
        index += 1


if __name__ == '__main__':
    start()
