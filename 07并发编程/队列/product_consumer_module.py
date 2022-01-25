from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(3):
        res = '包子%s' % i
        time.sleep(0.5)  # 模拟生产者造数据需要的时间
        print('生产者生产了%s' % res)
        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)


if __name__ == '__main__':
    # 容器
    q = Queue()
    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))
    p4 = Process(target=producer, args=(q,))
    # 消费之们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c3 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    c1.start()  # 程序会卡在q为空
    c2.start()
    c3.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # 有几个消费者就需要加几次None
    q.put(None)
    q.put(None)
    q.put(None)

    print('主程序')
'''此方法需要生产者消费者在一台机器上'''