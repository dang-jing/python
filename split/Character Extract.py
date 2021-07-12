# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 14:06
# @Author  : YangXiao
# @Project : 字符提取与消去
# @Software: PyCharm

import cv2
import os
import numpy as np

# from listname_txt import listname
# from namelist_txt import namelist

imgPath = ".\\img\\"
gtPath = ".\\txt\\"


imgs = os.listdir(imgPath)
gts = os.listdir(gtPath)
with open(".\\train.txt",'w',encoding='utf-8') as f:
    for i in range(len(imgs)):
        path1 = imgPath + imgs[i]   # img path
        path2 = gtPath + gts[i]    # gt path

        img = cv2.imdecode(np.fromfile(path1, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        # img = cv2.imread(path1)
        # print(img)

        # fileName = imgs[i][:]
        fileName = imgs[i][:-4]
        # print(fileName)
        if not os.path.exists('.\\result\\' + fileName):
            os.mkdir('.\\result\\' + fileName)
        k = 1
        for line in open(path2, encoding='utf-8'):
            rect = []
            line = line.strip('\n')
            arr = str.split(line, ',')
            name = arr[-1]
            #if name[0] == '\\':  # 可以将\保留
            name = name[0:]
            print(name)
            for j in range(8):
                rect.append(int(arr[j]))
                # rect.append(int(float(arr[j])))

            x1, y1, x2, y2, x3, y3, x4, y4 = rect

            ROI = img[y1:y3, x1:x3]
            # new_array = cv2.resize(ROI, (128, 256), interpolation=cv2.INTER_CUBIC)
            # print(ROI.size)

            i = 1

            if ROI.size != 0:
                if os.path.exists('.\\result\\' + fileName + '\\' + fileName + ' ' + str(i)+' ' + str(k)+ '.jpg'):  #  + str(k)+'_' + name
                    i += 1

                # cv2.imwrite('.\\result\\' + fileName + '\\' + fileName + '_' + str(i)+'_' + name + '.jpg', ROI)  # + str(i)
                # cv2.resize(img,(128,256))
                    cv2.imencode('.jpg', ROI)[1].tofile('.\\result\\' + fileName + '\\' + fileName + ' ' + str(i) + ' ' + str(k) + '.jpg') # +' ' + name
                    k += 1
                    print(name)
                    f.write(name + '\n')
                else:

                # cv2.imencode(保存格式, 保存图片)[1].tofile(保存路径)
                    cv2.imencode('.jpg', ROI)[1].tofile('./result/' + fileName + '/' + fileName + ' ' + str(i)+' '+ str(k) +'.jpg')
                # cv2.imwrite('.\\result\\' + fileName + '\\' + fileName + '_' + str(i)+'_' + name + '.jpg', ROI)
                    k += 1
                    print(name)
                    f.write(name + '\n')
f.close()
# listname()
# namelist()
print('Done')