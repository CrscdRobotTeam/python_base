import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(("127.0.0.1", 8080))

while True:  # 通信循环
    msg = input(">> ").strip()
    if not msg: continue
    phone.send(msg.encode("utf-8"))
    data = phone.recv(1024)
    print("服务端发来的消息", data.decode("utf-8"))

phone.close()

