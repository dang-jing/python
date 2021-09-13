# -*- coding:utf-8 -*-

import os

img_path = 'C:\\Users\\dangc\\Desktop\\a\\111\\'
txt_path = 'C:\\Users\\dangc\\Desktop\\a'
type = '.png'


img_dir = os.listdir(img_path)
txt_dir = os.listdir(txt_path)
for i in img_dir:
    name = i.split('.')[0]
    if name+'.txt' not in txt_dir:
        os.remove(img_path+name+type)
