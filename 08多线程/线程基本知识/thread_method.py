from threading import Thread, current_thread, active_count, enumerate
import time


def task():
    # current_thread()拿到当前线程对象
    print('%s is running ' % current_thread().getName())
    time.sleep(2)
    print('%s is done ' % current_thread().getName())


if __name__ == '__main__':
    # current_thread()获取的就是t
    t = Thread(target=task, name='子线程')
    t.setName('线程命名')  # 给线程重新命名
    t.start()
    # t.join()
    # current_thread().setName('kele')  # 主线程重新命名
    # print(active_count())
    # print(t.is_alive())
    # print('主线程', current_thread().getName())
    print(enumerate())  # 当前活跃的线程对象拿出来
