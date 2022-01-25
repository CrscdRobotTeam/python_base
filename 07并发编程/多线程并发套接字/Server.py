from socket import *
from multiprocessing import Process


def talk(conn):  #
    while True:
        try:
            data = conn.recv(1024)
            print(data)
            conn.send(data.upper())
        except ConnectionError:
            break
    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)

    while True:  # 主进程专门建立链接
        conn, addr = server.accept()
        p = Process(target=talk, args=(conn,))
        p.start()  # 子进程通讯

    server.close()


# windows 下开进程 一定要放在"__main__"下
if __name__ == '__main__':
    server('127.0.0.1', 8080)


#########################
'''
来一个，启一个进程，但是客户端可能存在上亿个，
服务端不可能在一个电脑上启动上亿个进程
启进程会占用内存
'''

#########################