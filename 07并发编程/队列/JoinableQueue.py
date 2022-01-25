from multiprocessing import Process, JoinableQueue
import time


def producer(q):
    for i in range(3):
        res = '包子%s' % i
        time.sleep(0.5)  # 模拟生产者造数据需要的时间
        print('生产者生产了%s' % res)
        q.put(res)
    q.join()  # 当消费者把所有东西都取完才执行


def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(1)
        print('消费者吃了%s' % res)
        q.task_done()  # 通知生产者有一个被取走了


if __name__ == '__main__':
    # 容器
    q = JoinableQueue()
    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))
    p4 = Process(target=producer, args=(q,))
    # 消费之们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c3 = Process(target=consumer, args=(q,))
    c1.daemon = True  # 守护进程，主进程执行完，清理
    c2.daemon = True
    c3.daemon = True

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    c1.start()  # 程序会卡在q为空
    c2.start()
    c3.start()

    # 保证都生产完
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    # 下一步主进程执行完，消费者消失
    print('主程序')
