# 写文件，
'''for i in range(5):
    into=input("\n\n请输入内容：")
    #r+替换掉原先的文件，w是先清空再重新写入
    f2 = open('D:\\图片\\测试.txt','a')
    f2.write(into+'\n')
    f2.close()'''


# 判断图片地址是否已经存在
# 文本中有换行符，要注意判断
def findURL(url):
    a = url + '\n'
    f = open('D:\\图片\\测试.txt')
    finder = False
    while True:
        str = f.readline()
        print(str)
        if str == a:
            print(a[0:-1], "-----------已存在")
            url = True
            break
        # readline读取到最后没数据时返回为空
        elif str == '':
            break
    return finder


import uuid
import os
import urllib.request


def urlPicture(image_url, file_path):
    # image_url = 'https://gss0.baidu.com/7Po3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=48bb1719d433c895a62b907de1235fc8/b2de9c82d158ccbf2b1ed5b414d8bc3eb0354199.jpg'
    # file_path = 'D:\\图片\\测试\\'
    # file_name = image_url
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)  # 如果没有这个path则直接创建
        file_suffix = uuid.uuid1()
        print(file_suffix)
        filename = '{}{}{}'.format(file_path, file_suffix, '.jpg')
        print(filename)
        urllib.request.urlretrieve(image_url, filename=filename)
        print(11111)
    except IOError as e:
        print(1, e)
    except Exception as e:
        print(2, e)


i = ['https://img0.baidu.com/it/u=1993732885,3339376170&fm=26&fmt=auto&gp=0.jpg',
     'https://img1.baidu.com/it/u=3679081981,3190695688&fm=26&fmt=auto&gp=0.jpg',
     'https://img2.baidu.com/it/u=4133805215,1291042303&fm=26&fmt=auto&gp=0.jpg',
     'https://img2.baidu.com/it/u=116038718,1630979763&fm=26&fmt=auto&gp=0.jpg',
     'https://img0.baidu.com/it/u=928870272,3732543784&fm=26&fmt=auto&gp=0.jpg',
     'https://img0.baidu.com/it/u=2148561412,1582299344&fm=26&fmt=auto&gp=0.jpg',
     'https://img1.baidu.com/it/u=193531869,262982413&fm=26&fmt=auto&gp=0.jpg',
     'https://img1.baidu.com/it/u=3273917651,620227061&fm=26&fmt=auto&gp=0.jpg',
     'https://img2.baidu.com/it/u=3513034976,2402641006&fm=26&fmt=auto&gp=0.jpg',
     'https://img2.baidu.com/it/u=984090628,2369479642&fm=26&fmt=auto&gp=0.jpg',
     'https://img1.baidu.com/it/u=491114851,3506616570&fm=26&fmt=auto&gp=0.jpg']
for i in i:
    print(i)
print("完成")