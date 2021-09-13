import pandas as pd
from kit.URLid import generate_id
#   生成代数uri，读取/写入excel


id = {'concepts': 34, 'rules': 58, 'relations': 12}
df = pd.read_excel(r'D:\b\代数知识图谱.xlsx', sheet_name='代数知识图谱')
name = df['中文命名']
lll = df['类型']
x = []
for i in range(len(name)):
    ss = generate_id.geometry('代数',name[i],lll[i])
    x.append(ss)
df = pd.DataFrame(df)
df.insert(0, 'aa', x)
df.to_excel(r'D:\b\example.xlsx', sheet_name='Sheet1', index=False, header=True)