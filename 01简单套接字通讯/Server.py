# 服务器端有两种套接字
import socket

# 1.买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
# 2.绑定手机卡（保证对方可以找到服务器）
# 127.0.0.1本地地址（运行server的机器的地址）回环地址，
# server和client运行在同一个机器上，client发送，server就能收到
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 解决端口被占用的问题
phone.bind(("127.0.0.1", 8080))  # 0-65535端口：0-1024给操作系统使用

# 3.开机
phone.listen(5)  # 5表示最大挂起的链接数为5

# 4.等电话链接
print("starting......")
# res是个对象，里面两个元素，表示客户端和服务器的链接，
# 前面为服务器信息，后面为客户端信息 # 服务端先启动，会卡在accept等待链接客户端
conn, client_addr = phone.accept()  # 有结果就会有值，建立链接
print("========>")
print(conn, client_addr)

# 5.收、发消息
while True:  # 通信循环
    try:  # 适用于 windows 用 try--except捕获异常
        data = conn.recv(1024)  # 1024代表接收最大为1024个字节的数据 1】单位bytes 2】1024代表最大接收1024bytes
        #if not data: break  # 适用于linux操作系统
        print("客户端的数据：", data)
        conn.send(data.upper())
    except ConnectionResetError:  # 连接异常
        break
# 6.挂电话
conn.close()

# 7.关机
phone.close()
