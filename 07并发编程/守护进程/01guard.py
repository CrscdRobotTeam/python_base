from multiprocessing import Process
import time


def task(name):
    print('%s is running' % (name))
    time.sleep(2)
    print('%s is over--->' % (name))
    # p = Process(target=time.sleep, args=(3,))#子线程下的子线程不允许开
    # p.start()


if __name__ == '__main__':
    p = Process(target=task, name='subprocess', args=('子进程1',))
    p1 = Process(target=task, name='subprocess', args=('子进程2',))
    p.daemon = True  # 设置守护进程， 一定要在进程开始之前设置
    p.start()
    p1.start()
    # p.join()
    print('主')
############################################
'''
守护进程，即伴随主进程
守护进程会在主进程代码执行结束后就终止
守护进程内无法再开启子进程,否则抛出异常：
AssertionError: daemonic processes are not allowed to have children
'''
#################################################
