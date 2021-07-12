import requests
from lxml import etree
import re
from queue import Queue
import threading


class ImageParse(threading.Thread):
    def __init__(self, page_queue, img_queue):
        super(ImageParse, self).__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers).text
        # print(response)
        html = etree.HTML(response)
        images = html.xpath('//div[@class="random_picture"]')
        for img in images:
            img_url = img.xpath('.//img/@data-original')
            # 获取图片名字
            print(img_url)
            alt = img.xpath('.//p/text()')
            for name, new_url in zip(alt, img_url):
                filename = re.sub(r'[?？.，。！!*\\/|]', '', name) + ".jpg"
                # 获取图片的后缀名
                # suffix = os.path.splitext(img_url)[1]
                # print(alt)
                self.img_queue.put((new_url, filename))


class Download(threading.Thread):
    def __init__(self, page_queue, img_queue):
        super(Download, self).__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            with open("表情包/" + filename, "wb")as f:
                response = requests.get(img_url).content
                f.write(response)
                print(filename + '下载完成')


def main():
    # 建立队列
    page_q = Queue()
    img_q = Queue()
    for x in range(1, 11):
        url = 'https://www.doutula.com/search?type=photo&more=1&keyword=%E7%A8%8B%E5%BA%8F%E5%91%98&page={}'.format(x)
        page_q.put(url)

    for x in range(5):
        t = ImageParse(page_q, img_q)
        t.start()
        t = Download(page_q, img_q)
        t.start()


if __name__ == '__main__':
    main()
