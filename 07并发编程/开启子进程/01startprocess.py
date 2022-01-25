# 进程就是程序执行的过程
# 开启一个qq，算开启一个进程
# run 01startprocess.py就是开启了一个进程 父进程
# 下面内容重点为，在进程01startprocess.py中再开一个进程

###########################方式一：##########################################
#
# from multiprocessing import Process  # Process是可开启进程对象的一个类
# import time
#
#
# def task(name):
#     print('%s is running' % name)
#     time.sleep(3)
#     print('%s is done' % name)
#
#
# # windows 系统需要把开启进程的指令放到'__main__'下
# if __name__ == '__main__':
#     p = Process(target=task, args=('子进程1',))  # args 按照位置传参数 加，代表元组
#     # Process(target=task, kwargs={'name': '子进程1'})  # kwargs 字典方式
#     # p为Process的对象
#     # 子进程
#     p.start()  # 给操作系统发送一个开启子进程的信号
#     # p.start()运行之后直接运行下面的程序，夫进程不会等待子进程
#     # 把父进程地址空间中的数据copy到子进程，作为子进程运行的初始状态
#     print("主进程")
#############################################################################

###########################方式二：##########################################

from multiprocessing import Process
import time


class MyProcess(Process):  # 新创建一个类，改写父类
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 名字一定为run
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is done' % self.name)


if __name__ == '__main__':
    p = MyProcess('子进程1')
    p.start()
    print('主进程')

#############################################################################
