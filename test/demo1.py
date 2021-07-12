import requests

'''response = requests.get(url="http://httpbin.org/ip")
#response = requests.get(url="http://imooc.com/")
print(response.text)
print(response.json()["origin"])'''

'''respons = requests.post(url="http://httpbin.org/post", data={"name": "imooc"})
print(respons.text)'''

# 主要用在get请求里
'''data = {"key1": "values"}
respons = requests.get("http://httpbin.org/get", params=data)
#查看当前请求的url是谁
print(respons.url)
print(respons.headers)'''

'''# 设置请求头
headers = {
    "user-agent": "imooc/v1"
}
response = requests.get(url="http://httpbin.org/ip", headers=headers)
print(response.request.headers) #查看请求头'''

'''# 设置超时时间,一般为1-2s
response = requests.get(url="url", TimeoutError=2)'''

'''查看百度的cookie
print(response.cookies)
print(response.cookies["BDORZ"])'''

'''cookies=dict(cookies_are="hello baidu")
#请求时带上cookies
response = requests.get(url="http://httpbin.org/cookies",cookies=cookies)
print(response.text)'''

#关闭ssl校验
response = requests.get(url="http://httpbin.org/cookies",verify=False)