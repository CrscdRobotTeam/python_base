from concurrent.futures import ThreadPoolExecutor
import requests, time


# 下载一个文件到本地来
def get(url):  # 网络 io类型
    response = requests.get(url)
    # print(response.text)  # 字符串
    time.sleep(3)  # 返回的快慢取决于网速
    return {'url': url, 'content': response.text}


def parse(res):
    res = res.result()
    print('%s parse res is %s'%(res['url'],len(res['content'])))


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'http://www.weather.com.cn/weather/101010100.shtml',
        'https://www.qq.com/'
    ]
    pool = ThreadPoolExecutor(2)
    for url in urls:
        pool.submit(get,url).add_done_callback(parse)

