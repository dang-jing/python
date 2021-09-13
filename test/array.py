

import os

listdir = os.listdir(r'C:\Users\dangc\Desktop\a\kg(1)(1)')
aa = []
for i in listdir:
    name = i.split(".")[0]
    aa.append(name)
print(aa)
