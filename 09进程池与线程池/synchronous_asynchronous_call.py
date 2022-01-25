# 提交任务的两种方式
# 1.同步调用:提交完，就在原地等待任务执行，等到返回结果，在执行下一行代码
# 程序串行执行

# from concurrent.futures import ThreadPoolExecutor
# import time, random
#
#
# def la(name):
#     print('%s is laing ' % name)
#     time.sleep(random.randint(3, 5))
#     res = random.randint(7, 13) * '#'
#     return {'name': name, 'res': res}
#
#
# def weight(shit):
#     name = shit['name']
#     size = len(shit['res'])
#     print('%s 拉 《%s》KG ' % (name, size))
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(13)
#
#     weight(pool.submit(la, 'alex').result())
#     weight(pool.submit(la, 'MMM').result())
#     weight(pool.submit(la, 'LLLL').result())
# 2.异步调用：提交完任务，不在原地等待
# 程序并行执行
from concurrent.futures import ThreadPoolExecutor
import time, random


def la(name):
    print('%s is laing ' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}
    # 这么些写类似于一个代码段，最好用回调函数，触发
    # weight( {'name': name, 'res': res})


def weight(shit):
    shit = shit.result()  # add_done_call(weight) 把对象中结果拿出来
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉 《%s》KG ' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    # pool.submit(la, 'alex') 返回一个对象传给add_done_callback(weight)
    pool.submit(la, 'alex').add_done_callback(weight)
    pool.submit(la, 'MMM').add_done_callback(weight)
    pool.submit(la, 'LLLL').add_done_callback(weight)
'''阻塞遇到io操作'''