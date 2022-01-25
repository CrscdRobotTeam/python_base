# mutex 保护不同的数据需要加不同的锁

from threading import Thread, current_thread,Lock
import time

n = 100


def task(mutex):
    global n
    mutex.acquire()
    temp = n
    time.sleep(0.5)
    n = temp - 1

    mutex.release()
    print('线程%s n=%s', current_thread().getName(), n)

if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(50):
        t = Thread(target=task,args=(mutex,))
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    print('主 n=', n)
