# 客户端只有一种套接字
import socket

# 1.买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)

# 2.拨号
phone.connect(("127.0.0.1", 8080))

# 3.收、发消息
while True:  # 通信循环
    msg = input(">> ").strip()
    if not msg: continue
    phone.send(msg.encode("utf-8"))  # 不能直接发字符串，需转到物理层 encode编码
    data = phone.recv(1024)
    print("服务端发来的消息", data.decode("utf-8"))  # decode解码
# 当msg为""空时，即直接回车，phone.send(b"")，recv(1024)不能收到空数据
# 4.关机
phone.close()
# recv和send都是跟操作系统说，让其调用网卡收发数据，因为应用程序不能直接调用硬件
