# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# import os, time, random
#
#
# def task(name):
#     print('name: %s pid:%s run' % (name, os.getpid()))
#     time.sleep(random.randint(1, 3))
#
#
# if __name__ == '__main__':
#
#     '''进程池（4指定进程池的大小，默认为cpu核数）'''
#     pool = ProcessPoolExecutor(4)  # 池子里就四个进程
#
#     for i in range(10):
#         # p = Process(target=task, args=('进程%s' % i,))
#         # p.start()
#         pool.submit(task, '进程%s' % i)  # 异步调用方式提交任务，
#                                     # 不用在原地等任务执行，拿到返回结果
#     pool.shutdown(wait=True)  # 不能再往进程池放任务了 默认wait=True，
#                             # 等进程池执行完在执行后面的代码
#     print('主')
# '''进程池作用，造对象，开启对象'''


from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import current_thread
import os, time, random


def task():
    print('name:%s pid:%s run' % (current_thread().getName(), os.getpid()))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    for i in range(10):
        pool.submit(task, )
    pool.shutdown()  # wait=True
    print('主')
