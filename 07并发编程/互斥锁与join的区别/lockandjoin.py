from multiprocessing import Process
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


def task(name):
    search(name)  # 查票是并发操作
    get(name)


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task, args=('路人%s' % i, ))
        p.start()
        p.join()

        '''join可以保证数据安全，但是join把整个进程都变成串行的了'''
        '''
        互斥锁可以把局部的某些部分变成串行的，也就是把并发修改数据那部分变成串行，
        降低程序运行效率，保证数据安全
        '''
        '''通过文件的方式，实现进程之间共享数据'''
        '''进程运行内存是互相隔离的，但是硬盘数据是共享的，但是读写效率低'''
        '''共享就需要加锁，加锁要在合适的时候加，用完要释放，要不其他进程或程序没法正常干活'''
        '''
        共享内存，可以提升共享数据读写的效率，还可以解决枷锁的问题  
        IPC模块，队列和管道，一块共享的内存
        队列 就是 管道加锁实现的
        '''
