import socket
import subprocess
import struct
import json  # 序列化可将python的数据结构转化成json的数据结构
import os

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
            res = conn.recv(8096)  # b"get a.txt"，一种自定义的bytes串

            # 2.解析命令（把用户传过来的命令变成格式化的命令），提取相应命令参数
            #################系统命令#############################################
            # obj = subprocess.Popen(cmd.decode("utf-8"), shell=True,
            #                        stdout=subprocess.PIPE,
            #                        stderr=subprocess.PIPE)
            # stdout = obj.stdout.read()
            # stderr = obj.stderr.read()####现在不用系统命令，要用软件程序自定义命令
            #####################################################################
            cmds = res.decode("utf-8").split()  # ['get','a.txt']拿到这个列表
            filename = cmds[1]
            # 3.以读的方式打开文件，发给客户端
            # with open(filename,'rb') as f:
            #     conn.send(f.read()) # 会出现粘包问题
            # 【1】制作固定长度的报头
            header_dic = {
                "filename": filename,
                "md5": "xxdxx",
                "file_size": os.path.getsize(filename)  # 获取文件大小
            }
            header_json = json.dumps(header_dic)  # 把字典转化为json字符串
            header_bytes = header_json.encode("utf-8")  # 把json字符串转化为bytes，供发送使用，send只能发送bytes

            # 【2】先发送报头的长度
            conn.send(struct.pack("i", len(header_bytes)))  # 把报头长度转化为固定长度
            # 【3】发报头
            conn.send(header_bytes)

            # 【4】发送真实的数据
            with open(filename, 'rb') as f:
                # conn.send(f.read())#当文件非常大，全读出，内存会占满，崩溃
                for line in f:
                    conn.send(line)  # 节省内存，文件自动粘包
        except ConnectionResetError:  # 连接异常
            break

    conn.close()

phone.close()
