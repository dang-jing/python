# -*-coding:utf-8-*-


import re
import time

import requests
import os

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36",
    "upgrade-insecure-requests": "1",
}

qid = 'http://cstore-private-bs.seewo.com/easinote/encloud-16228838964774ac26ce7?Expires=1628229009&OSSAccessKeyId=LTAI4gvNbAt0Hvya&Signature=zTIOCfFVcxxBceirzyaz8vBKu2c%3D'  # 这里是网页视频的url地址
page = requests.get(qid, headers=headers)
ret = page.content

timec = int(time.time())
with open(r'C:\Users\dangc\Desktop\a\全等三角形%d.mp4' % timec, 'wb') as f:  # 用时间戳命名文件名
    f.write(ret)
