import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 解决端口被占用的问题
phone.bind(("127.0.0.1", 8080))  # 0-65535端口：0-1024给操作系统使用
phone.listen(5)  # 5表示最大挂起的链接数为5，最多运行5个Client，
# 现在只能一个一个服务，但是可以开启共五个客户端
conn, client_addr = phone.accept()  # 有结果就会有值，建立链接

while True:
    try:  # 适用于 windows 用 try--except捕获异常
        # 1.接收命令
        msg = conn.recv(1024)
        if not msg: break
        else:print("客户端的数据1：", msg.decode("GBK"))
        # time.sleep(6)#5s
        # msg = conn.recv(1024)
        # print("客户端的数据2：", msg.decode("GBK"))


    except ConnectionResetError:  # 连接异常
        phone.close()

conn.close()
phone.close()
