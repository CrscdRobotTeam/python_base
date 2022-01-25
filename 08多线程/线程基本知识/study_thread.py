##################开线程方法一：###########################
# from threading import Thread
# import time
# import random
#
#
# def piao(name):
#     print('%s piaoing' % name)
#     time.sleep(random.randrange(1, 5))
#     print('%s piao end' % name)
#
#
# if __name__ == "__main__":
#     t1 = Thread(target=piao, args=('egon',))
#     t1.start()
#     print('主线程')  # 从资源角度主进程，从执行角度主线程
#######现在程序里有两个线程#########
'''
进程，运行独立，占用独立的空间，其内部运行信息，其他进程不知道
类似于同一个公司的不同部门
但是部门自己并不能工作
部门需要有相关人员，指的就是线程
'''
'''
每启动一个进程，其中至少有一个线程
进程本身只是内存资源占用，并不能执行
同一进程的多个线程共享进程的资源
启进程需要占用内存空间，启线程就是运用进程已经取得的线程
'''
'''
一个文件执行的时候，相当于启动一个进程，默认包含一个线程
一个进程想要执行，默认需要有一个线程
'''
##################开线程方法二：###########################
from threading import Thread
import time
import random


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s piaoing' % self.name)
        time.sleep(random.randrange(1, 5))
        print('%s piao end' % self.name)


if __name__ == "__main__":
    t1 = MyThread('egon')
    t1.start()
    print('主线程')  # 从资源角度主进程，从执行角度主线程
