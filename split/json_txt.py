import math
import os
import json
import numpy as np
# def main():
def json2txt(path_json, path_txt):
    with open(path_json, 'r', encoding='utf-8') as path_json:  # gb18030
        jsonx = json.load(path_json)
        i = 0
        with open(path_txt, 'w+', encoding='utf-8') as ftxt:
            for shape in jsonx['shapes']:
                xy = np.array(shape['points'])
                # x = np.array()
                label = str(shape['label'])
                strxy = ''
                for m, n in xy:

                    if i == 0:
                        strxy += str(int(m)) + ',' + str(int(n)) + ','
                        strxy += str(math.ceil(shape['points'][1][0])) + ','
                        strxy += str(int(n)) + ','
                        i = i + 1
                    else:
                        strxy += str(math.ceil(m)) + ',' + str(math.ceil(n)) + ','
                        strxy += str(int(shape['points'][0][0])) + ','
                        strxy += str(math.ceil(n)) + ','
                i = 0
                strxy += label
                ftxt.writelines(strxy + "\n")


#dir_json = r'C:\Users\dangc\Pictures\2选择\\'
#dir_txt = r'D:\python\demo\split\txt\\'
'''if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
    print(dir_txt)
list_json = os.listdir(dir_json)
for cnt,json_name in enumerate(list_json):
    print('cnt=%d,name=%s'% (cnt, json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json','.jpg.txt')  # .jpg
    # print(path_json, path_txt)
    json2txt(path_json, path_txt)'''

'''if __name__ == '__main__':
    main()'''
