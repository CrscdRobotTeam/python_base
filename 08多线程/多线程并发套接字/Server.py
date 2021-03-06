# from socket import *
# from threading import Thread
#
#
# def communicate(conn):
#     while True:
#         try:
#             data=conn.recv(1024)
#             if not data:break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     conn.close()
#
#
# def server(ip,port):
#     server = socket(AF_INET, SOCK_STREAM)
#     server.bind((ip, port))
#     server.listen(5)
#
#     while True:
#         conn, addr = server.accept()
#         t = Thread(target=communicate,args=(conn,))
#         t.start()
#     server.close()
#
#
# if __name__=='__main__':
#     server('127.0.0.1',8080)

'''问题，现在服务端运行在一台电脑上，一台电脑不能无限开线程'''
'''用线程池或进程池解决上面的问题，管理开线程的数量'''

from concurrent.futures import ThreadPoolExecutor
from socket import *


def communicate(conn):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip,port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        # t = Thread(target=communicate,args=(conn,))
        # t.start()
        pool.submit(communicate,conn)
    server.close()


if __name__=='__main__':
    pool = ThreadPoolExecutor(2)
    server('127.0.0.1',8080)