import pandas as pd
import uuid
#   读取excel，生成uri并写入新的excel内


#   id命名规范:id.png

#   不同类型对应id最大的值        注意代码执行完毕要修改 {'concepts': 34, 'rules': 57, 'relations': 12}
id = {'concepts': 34, 'rules': 58, 'relations': 12}
df = pd.read_excel(r'C:\Users\dangc\Desktop\a\知识图谱-id增加情况.xlsx', sheet_name='三角形知识图谱')
name = df['中文命名']
lll = df['类型']
x = []
for i in range(len(name)):
    ss = ''
    if '定义' == lll[i]:
        ss = 'axskg:math/geometry/concepts/' + name[i]
        concepts = id['concepts']
        con = bin(concepts)[2:]
        len1 = len(con)
        eee = ''
        for i in range(16 - len1): eee += '0'
        len1 = eee + con
        len1 = int('0001001000000001' + len1, 2)
        ss = ss + '#' + str(len1)
        id['concepts'] = concepts + 1
    elif '定理' == lll[i]:
        ss = 'axskg:math/geometry/rules/' + name[i]
        concepts = id['rules']
        con = bin(concepts)[2:]
        len1 = len(con)
        eee = ''
        for i in range(16 - len1): eee += '0'
        len1 = eee + con
        len1 = int('0001001000000100' + len1, 2)
        ss = ss + '#' + str(len1)
        id['rules'] = concepts + 1
    elif '关系' == lll[i]:
        ss = 'axskg:math/geometry/relations/' + name[i]
        concepts = id['relations']
        con = bin(concepts)[2:]
        len1 = len(con)
        eee = ''
        for i in range(16 - len1): eee += '0'
        len1 = eee + con
        len1 = int('0001001000000010' + len1, 2)
        ss = ss + '#' + str(len1)
        id['relations'] = concepts + 1
    else:
        ss = 'axskg:math/geometry/rules/' + name[i]
        concepts = id['rules']
        con = bin(concepts)[2:]
        len1 = len(con)
        eee = ''
        for i in range(16 - len1): eee += '0'
        len1 = eee + con
        len1 = int('0001001000000100' + len1, 2)
        ss = ss + '#' + str(len1)
        id['rules'] = concepts + 1
    x.append(ss)
df = pd.DataFrame(df)
df.insert(0, 'aa', x)
#   print(df)
print('记得修改id的json内容哦,修改如下：', id)
'''for i in x:
    df.loc['英文'] = i
print(df)'''
df.to_excel(r'C:\Users\dangc\Desktop\a\example.xlsx', sheet_name='Sheet1', index=False, header=True)
