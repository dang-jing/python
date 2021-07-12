import requests
import json

def parsing_URL():
    query="刘德华"
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7971024659633359185&ipn=rj&ct=201326592&is=&fp=result&queryWord="+query+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word="+query+"&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=120&rn=30&gsm=78&1621584374169=";
    # url="https://pic.sogou.com/napi/pc/searchList?mode=1&start=2300*48&xml_len=48&query=%E5%88%9D%E4%B8%AD%E6%95%B0%E5%AD%A6%E9%A2%98";
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    #获取网页信息，verify关闭ssl校验
    response = requests.get(url=url, headers=headers, verify=False)
    '''print(response.text)
    print(response.headers)
    print(response.request.headers)'''
    #拿到请求页面发布会的所有内容
    jsonobj = json.loads(response.text)
    imgPaths = jsonobj['data']
    print(imgPaths)
    imgList = []
    a = 0
    # 拿到所有的图片源地址放入集合中
    for imgPath in imgPaths:
        # print(imgPath)
        if imgPath == {}:
            break
        imgList.append(imgPath['thumbURL'])
        a += 1
        print(imgPath['thumbURL'])
    return imgList

#十进制转为十六进制
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])
print(parsing_URL())