##################### join 方法 ####################################
# from multiprocessing import Process
# import time, os
#
#
# def task():
#     print('id %s is running , parent id is <%s>' % (os.getpid(), os.getppid()))
#     time.sleep(3)
#     print('id %s is done, parent id is <%s>' % (os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':
#     p = Process(target=task, )
#     p.start()
#     p.join()  # p.join() 保证子进程先结束
#                 # 主进程等子进程运行结束，再往下执行，
#     print("主进程 <%s> 子进程 %s" % (os.getppid(), os.getpid()))
#     print(p.pid) # p进程已经运行结束，还是可以看pid 即僵尸进程
###################################################################################

############################ 并行 #################################################
# from multiprocessing import Process
# import time, os
#
#
# def task(name):
#     print('%s ----- id %s is running , parent id is <%s>' % (name, os.getpid(), os.getppid()))
#     time.sleep(3)
#     print('%s ----- id %s is done, parent id is <%s>' % (name, os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':
#     start = time.time()
#     p0 = Process(target=task, args=('子进程0',))
#     p1 = Process(target=task, args=('子进程1',))
#     p2 = Process(target=task, args=('子进程2',))
#     p3 = Process(target=task, args=('子进程3',))
#     p4 = Process(target=task, args=('子进程4',))
#
#     # 向操作系统发送开启请求
#     p0.start()
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     p0.join()
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#
#     # 主进程等子进程运行结束，再往下执行，
#     print("主进程 <%s> 子进程 %s" % (os.getppid(), os.getpid()))
#     print(time.time()-start)  # p进程已经运行结束，还是可以看pid 即僵尸进程
######################################################################################

######################## 串行 ########################################################
from multiprocessing import Process
import time, os


def task(name):
    print('%s ----- id %s is running , parent id is <%s>' % (name, os.getpid(), os.getppid()))
    time.sleep(3)
    print('%s ----- id %s is done, parent id is <%s>' % (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    start = time.time()
    p0 = Process(target=task, args=('子进程0',))
    p1 = Process(target=task, args=('子进程1',))
    p2 = Process(target=task, args=('子进程2',))
    p3 = Process(target=task, args=('子进程3',))
    p4 = Process(target=task, args=('子进程4',))
    # p4 = Process(target=task, name='sub_process')#name 给线程命名
    # 向操作系统发送开启请求
    # p0.start()
    # p0.join()
    #
    # p1.start()
    # p1.join()
    #
    # p2.start()
    # p2.join()
    #
    # p3.start()
    # p3.join()
    #
    # p4.start()
    # p4.join()

    p_l = [p0, p1, p2, p3, p4]
    for p in p_l:
        p.start()
    p0.terminate()  # 关掉子进程0，但是没有效果，只是给操作系统发了信号，
    # 因为进程的开启、关闭由系统管理，系统执行关掉进程，也是需要花费时间的
    # time.sleep(3)之后可能关闭了
    print(p0.is_alive())
    for p in p_l:
        p.join()

    # 主进程等子进程运行结束，再往下执行，
    print("主进程 <%s> 子进程 %s" % (os.getppid(), os.getpid()))
    print(time.time() - start)  # p进程已经运行结束，还是可以看pid 即僵尸进程
    print(p0.is_alive())

# 进程间内存空间是隔离的
