from multiprocessing import Process

n = 100


def work():
    global n
    n = 0
    print('子进程 n=', n)


if __name__ == '__main__':
    p = Process(target=work, name='subprocess')
    p.start()
    p.join()
    print('主进程 n=', n)
