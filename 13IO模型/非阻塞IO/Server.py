from socket import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
server.setblocking(False)  # 非阻塞，运行完此行，
# 下面所有的IO操作都变成非阻塞
recv_l = []
send_l = []
while True:
    try:
        conn, addr = server.accept()  # BlockingIOError:
        recv_l.append(conn)
        print(recv_l)
    except BlockingIOError:
        # print('other things')

        # 收消息
        del_recv_l = []
        for conn in recv_l:  # 循环过程中不能改变迭代对象
            try:
                data = conn.recv(1024)
                if not data:
                    del_recv_l.append(conn)
                    continue
                # conn.send(data.upper())  # 在数据量大的时候也会有阻塞
                send_l.append((conn, data.upper()))  # 存放套接字和套接字要发送的数据的元组
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_recv_l.append(conn)

        for conn in del_recv_l:
            recv_l.remove(conn)

        # 发消息
        del_send_l = []
        for item in send_l:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)  # IO操作，可能抛出异常
                del_send_l.append(item)
            except BlockingIOError:
                # continue
                pass

        for item in del_send_l:
            send_l.remove(item)

server.close()

'''链接可能得不到相应，线程一直处于就绪状态，一直占着cpu'''