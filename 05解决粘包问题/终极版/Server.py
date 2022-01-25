import socket
import subprocess
import struct
import json  # 序列化可将python的数据结构转化成json的数据结构

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 解决端口被占用的问题
phone.bind(("127.0.0.1", 8080))  # 0-65535端口：0-1024给操作系统使用

phone.listen(5)  # 5表示最大挂起的链接数为5，最多运行5个Client，
# 现在只能一个一个服务，但是可以开启共五个客户端

print("starting......")

while True:  # 链接循环
    # 服务端能一个一个服务客户端
    conn, client_addr = phone.accept()  # 有结果就会有值，建立链接
    print("========>")
    print(conn, client_addr)

    while True:  # 通信循环
        try:  # 适用于 windows 用 try--except捕获异常
            # 1.接收命令
            cmd = conn.recv(8096)
            print("客户端的数据：", cmd)
            # 2.执行命令，拿到结果  系统命令
            obj = subprocess.Popen(cmd.decode("utf-8"), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 3.把命令的结果返回给客户端
            # 【1】制作固定长度的报头
            header_dic = {
                "filename": "a.txt",
                "md5": "xxdxx",
                "total_size": len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_dic)  # 把字典转化为json字符串
            header_bytes = header_json.encode("utf-8")  # 把json字符串转化为bytes，供发送使用，send只能发送bytes

            # 【2】先发送报头的长度
            conn.send(struct.pack("i", len(header_bytes)))#把报头长度转化为固定长度
            # 【3】发报头
            conn.send(header_bytes)

            # 【4】发送真实的数据
            conn.send(stdout)
            conn.send(stderr)  # TCP会自动粘包
        except ConnectionResetError:  # 连接异常
            break

    conn.close()

phone.close()
