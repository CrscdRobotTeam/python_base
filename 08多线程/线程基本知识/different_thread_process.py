#
# 1.开进程的开销远大于开线程

# from multiprocessing import Process
# from threading import Thread
# import time
#
#
# def piao(name):
#     print('%s piaoing' % name)
#     time.sleep(2)
#     print('%s piao end' % name)
#
#
# if __name__ == "__main__":
#     t1 = Thread(target=piao, args=('egon',))
#     t1.start()
#     # p1 = Process(target=piao, args=('egon',))
#     # p1.start()
#
#     print('主线程')  # 从资源角度主进程，从执行角度主线程
######################### 输出结果 ##########################
# Process
'''
主线程
egon piaoing #开启的进程，在主进程后
egon piao end
'''
# Thread
'''
egon piaoing #开启的线程，在主进程前
主线程
egon piao end
'''
# 2.同一个进程内多个线程共享线程的地址空间

# from multiprocessing import Process
# from threading import Thread
# import time
#
# n = 100
#
#
# def task():
#     global n
#     n = 0
#     print('子进程 n=', n)
#
#
# if __name__ == "__main__":
#     # p1 = Process(target=task,) # 子进程copy 主进程地址空间中的数据
#     # p1.start()
#     # p1.join()
#
#     t1 = Thread(target=task,) # 子线程共享进程数据
#     t1.start()
#     t1.join()
#     print('主线程 n=',n)  # 从资源角度主进程，从执行角度主线程
#######输出结果
# Process
'''
子进程 n= 0
主线程 n= 100
'''
# Thread
'''
子进程 n= 0
主线程 n= 0
'''
# 3.pid
from multiprocessing import Process, current_process
from threading import Thread
import os

def task():
    #print('子进程 pid =', current_process().pid)
    #print('子进程 pid = %s 父进程 ppid = %s' %(os.getpid(),os.getppid()))
    print('线程 pid = %s 父进程 ppid = %s' %(os.getpid(),os.getppid()))

if __name__ == "__main__":
    # p1 = Process(target=task, )  # 子进程copy 主进程地址空间中的数据
    # p1.start()

    t1 = Thread(target=task,) # 子线程共享进程数据
    t1.start()
    t1.join()
    #print('主线程 pid =', current_process().pid)  # 从资源角度主进程，从执行角度主线程
    print('主线程 pid =', os.getpid()) # 获取当前线程的pid