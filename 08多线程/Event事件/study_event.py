from threading import Thread, Event, current_thread
import time

event = Event()

# event.wait() # 原地等待，等到set为止
# event.set()
# event.wait()
# def student():
#     print('学生 %s 正在听课' % current_thread().getName())
#     #event.wait()
#     '''wait 可设置超时事件，如果在规定的时间内，没有接受到set信号，会自动向下执行'''
#     event.wait(2)
#     print('学生 %s 课间活动' % current_thread().getName())
#
#
# def teacher():
#     print('老师 %s 正在授课' % current_thread().getName())
#     time.sleep(7)
#     print('老师 %s 结束授课' % current_thread().getName())
#     event.set()
#
#
# if __name__ == '__main__':
#     s_l = []
#     for i in range(3):
#         stu = Thread(target=student)
#         s_l.append(stu)
#         t = Thread(target=teacher)
#     for stu in s_l:
#         stu.start()
#     t.start()

from threading import Thread, Event, current_thread
import time

event = Event()


def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print('%s try %s times 结束了' % (current_thread().getName(), n))
            return # 到达最大次数，结束函数
        print('%s try %s ' % (current_thread().getName(), n))
        event.wait(0.5)  # 继续向下执行
        n += 1
    print('%s is connected ' % current_thread().getName())


def check():
    print('%s is checking ' % current_thread().getName())
    time.sleep(5)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()
    t = Thread(target=check)
    t.start()
