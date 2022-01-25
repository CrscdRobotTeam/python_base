# 进程开启后需要操作系统去管理，
# 它会给每个进程一个编号即进程id，简称pid
# 查看子进程id--pid 查看子进程的父进程id -- ppid
# 主进程会等子进程运行完了，再结束
# 子进程运行结束后不会直接清空内存信息，会留下一些运行状态信息如pid，
# 等待父进程随时查看子进程的运行状态
# 父进程结束之后会掉用一个函数，将所有僵尸进程清理
# 父进程如果一直不死，可能导致有很多僵尸进程，
# 占用很多pid，影响操作系统再生成子进程（此种情形，僵尸进程有害）

# 孤儿进程无害

from multiprocessing import Process
import time, os


class MyProcess(Process):  # 新创建一个类，改写父类
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 名字一定为run
        print('%s is running ,parent id is <%s>' % (os.getpid(), os.getppid()))
        time.sleep(3)
        print('%s is done' % os.getpid())


if __name__ == '__main__':
    p = MyProcess('子进程1')
    p.start()
    print('主进程 %s is done' % os.getpid())

# def task():
#     print('%s is running' % os.getpid())
#     time.sleep(3)
#     print('%s is done' % os.getpid())

# if __name__ == '__main__':
#     p = Process(target=task,)
#     p.start()
#     print("主进程")
