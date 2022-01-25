from multiprocessing import Process, Lock
import json
import time


def search(name):
    time.sleep(1)  # 查票命令提交给后台的网络延时模拟
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))  # 读取数据库（文件）操作
    print('<%s> 查看剩余得票数 {%s}' % (name, dic['count']))


def get(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(3)  # 购票提交回数据库延时模拟
        json.dump(dic, open('db.txt', 'w', encoding='utf-8'))  # 写入数据库（文件）操作
        print('<%s>购票成功' % name)
    else:
        print('<%s>购票失败' % name)


def task(name, mutex):
    search(name)  # 查票是并发操作

    mutex.acquire()
    get(name)
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = Process(target=task, args=('路人%s' % i, mutex))
        p.start()
