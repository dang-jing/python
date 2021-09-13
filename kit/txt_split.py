# -*- coding:utf-8 -*-

# 在文本文件中看是否有该url地址，有的话返回true

txtPath = r'C:\Users\dangc\Desktop\a\ActaM_1970_37_63.math'
newtxt_dir = 'C:\\Users\\dangc\\Desktop\\a\\111\\'


Path = open(txtPath)
for str in Path:
    # 单行读取文件内容
    label = str.split(',')[0]
    #   追加文本
    f2 = open(newtxt_dir + label + '+1.txt', 'a')
    f2.write(str)
    '''if str == a:
        print(a[0:-1], "-----------已存在")
        finder = True
        break'''
# readline读取到最后没数据时返回为空
# 读取文件内容为空时，跳出循环体
    if str == '':
        break
