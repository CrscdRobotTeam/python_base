# 基于gevent实现套接字
from gevent import monkey, spawn  # spawn提交线程对象

monkey.patch_all()
from socket import *


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()  # io 明显等待 等待连接
        # t = Thread(target=communicate,args=(conn,))
        # t.start()
        spawn(communicate, conn)
    server.close()


if __name__ == '__main__':
    g = spawn(server, '127.0.0.1', 8080)
    g.join()
