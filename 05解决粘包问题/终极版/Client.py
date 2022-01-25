import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(("127.0.0.1", 8080))

while True:  # 通信循环
    # 1.发命令
    cmd = input(">> ").strip()
    if not cmd: continue
    phone.send(cmd.encode("utf-8"))
    # 2.拿命令的结果，并打印
    # 【1】收报头长度
    header_size = struct.unpack("i", phone.recv(4))[0]
    # 【2】收报头
    header_bytes = phone.recv(header_size)
    # 【3】解析报头数据
    header_json = header_bytes.decode("utf-8")
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic["total_size"]

    # 【3】接收真时的数据
    recv_size = 0
    recv_data = b""
    while recv_size < total_size:
        res = phone.recv(100)  # 数字最大也就是操作系统的缓存数量
        recv_data += res
        recv_size += len(res)
    print("服务端发来的消息", recv_data.decode("GBK"))

phone.close()
