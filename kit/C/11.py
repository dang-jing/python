import pandas as pd
from kit.URLid import generate_id

if __name__ == '__main__':
    print(generate_id.geometry('几何', '线段包含', '内部实现', '定理'))
    '''ss = '0001001000000100'
    l = list(ss)
    l[11] = '1'
    ss = ''.join(l)
    print(ss)
    print(type(ss))'''


def aa():
    df = pd.read_excel(r'C:\Users\dangc\Desktop\a\三角形知识图谱.xlsx', sheet_name='三角形知识图谱')
    relations = df['关系描述']
    print(relations[1].split('\n')[0])