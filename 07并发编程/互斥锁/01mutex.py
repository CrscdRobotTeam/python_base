from multiprocessing import Process, Lock
import time


def task(name, mutex):
    mutex.acquire()
    print('%s 1---->' % name)
    time.sleep(1)
    print('%s 2---->' % name)
    time.sleep(1)
    print('%s 3---->' % name)
    mutex.release()


if __name__ == '__main__':
    '''   
    互斥锁保证数据不错乱
    保证所有进程共用同一把锁
    '''
    mutex = Lock()  #
    for i in range(3):
        '''开始运行谁先抢到锁谁先运行task'''
        p = Process(target=task, args=('进程%s' % i, mutex))
        p.start()

'''
进程自己的运行空间是独立的，但是可以访问同一个文件
共享带来的问题就是竞争、竞争带来的问题就是错乱
'''
