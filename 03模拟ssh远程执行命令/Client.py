import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(("127.0.0.1", 8080))

while True:  # 通信循环
    #1.发命令
    cmd = input(">> ").strip()
    if not cmd: continue
    phone.send(cmd.encode("utf-8"))
    #2.拿命令的结果，并打印
    data = phone.recv(1024)#如果大于1024，只能收到1024个bytes
    print("服务端发来的消息", data.decode("GBK"))

phone.close()

