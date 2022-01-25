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
    # 2.以写的方式打开一个新文件，接收服务器发来的文件，写入新打开的文件中
    # 【1】收报头长度
    header_size = struct.unpack("i", phone.recv(4))[0]
    # 【2】收报头
    header_bytes = phone.recv(header_size)
    # 【3】解析报头数据
    header_json = header_bytes.decode("utf-8")
    header_dic = json.loads(header_json)
    print(header_dic)
    filename = r"E:\PyProject\06文件传输\简单版\b.docx"
    file_size = header_dic["file_size"]

    # 【3】接收真时的数据
    with open(filename, 'wb') as f:
        recv_size = 0
        # recv_data = b""
        while recv_size < file_size:
            line = phone.recv(1024)  # 数字最大也就是操作系统的缓存数量
            # recv_data += res
            f.write(line)
            recv_size += len(line)
            print('文件总大小：%s 已下载的大小：%s '%(file_size,recv_size))
    # print("服务端发来的消息", recv_data.decode("GBK"))  # 打印到控制台

phone.close()
