# from threading import Thread
# import time
#
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi, args=('egon',))
#     #t.setDaemon(True)  # 必须在t.start()之前设置
#     #t.daemon = True
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())


from threading import Thread
import time

def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3) # 主线程等待此线程执行
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")
'''守护线程，主线程结束就结束，非守护线程，主线程，需要等其他线程都执行完了，主线程结束'''