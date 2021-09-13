import pandas as pd
import json
import uuid

#   id命名规范:id.png

#   不同类型对应id最大的值        注意代码执行完毕要修改 {'concepts': 34, 'rules': 57, 'relations': 12}
id = {'concepts': 34, 'rules': 58, 'relations': 12}
df = pd.read_excel(r'D:\b\三角形知识图谱 .xlsx', sheet_name='三角形知识图谱')
name = df['中文命名']
lll = df['教材分布']
print(name,lll)

js = dict()
for i in range(len(lll)):
    js[name[i]] = lll[i]
print(js)
json_str = json.dumps(js, ensure_ascii=False)
with open(r'D:\b\1.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)
