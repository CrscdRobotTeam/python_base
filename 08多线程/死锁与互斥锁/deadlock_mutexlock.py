# from threading import Thread, Lock
# import time

# 实例化两次得到不同的锁
# mutexA = Lock()
# mutexB = Lock()
#
#
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print('%s 拿到了A锁' % self.name)
#         mutexB.acquire()
#         print('%s 拿到了B锁' % self.name)
#         mutexB.release()
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print('%s 拿到了B锁' % self.name)
#         time.sleep(0.1)
#         mutexA.acquire()
#         print('%s 拿到了A锁' % self.name)
#         mutexA.release()
#         mutexB.acquire()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()  # 开线程的开销非常小，几乎是提交start的同时开启了
'''
输出结果
Thread-1 拿到了A锁
Thread-1 拿到了B锁
Thread-1 拿到了B锁
Thread-2 拿到了A锁
'''
# 线程卡住了，1想拿a锁，2想拿b锁，造成死锁现象
'''互斥锁只能acquire()一次，想要再acquire需要先release()'''

'''用 递归锁 解决上面的 死锁 问题'''

from threading import Thread, RLock
import time

mutexB = mutexA = RLock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(1)
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
'''
递归锁，可以连续require，
每acquire一次，计数器+1，只要计数不为0，就不能被其它线程抢到
'''