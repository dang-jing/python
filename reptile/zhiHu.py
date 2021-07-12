# -*_coding:utf8-*-
import requests
from lxml import etree
from imp import reload
import sys
reload(sys)


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    response = requests.get(url="http://www.zhongkao.com/e/20210107/5ff718d481d46_14.shtml", headers=headers,
                            verify=False)
    response.encoding = 'utf-8'
    response = response.content
    label = etree.HTML(response)
    content = label.xpath('//h1[@class="ft20 center"]a/text()')
    print(content[0])
