# windows：
# dir：查看某一文件夹下的子文件名与子文件夹名
# ipconfig：查看本地网卡的IP信息
# tasklist：查看运行的进程


# linux：
# ls
# ifconfig
# ps aux


# 执行系统命令,并且拿到结果
# import os
# #res返回结果为命令是否执行成功，
# # 0为成功，非0为不成功
# res = os.system("dir E:\PyProject")

import subprocess

# shell = True 命令解释器，类似于开启一个cmd
# stdout = subprocess.PIPE,正确的结果丢到管道里，管道左边进数据，右端取数据
# stderr = subprocess.PIPE,错误的结果丢到另一个管道里
obj = subprocess.Popen("dir E:\PyProject", shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
# obj是各个对象,"GBK"windows默认编码，"utf-8"linux默认的编码
print(obj)
print("stdout 1----->", obj.stdout.read().decode("GBK"))
print("stderr 2----->", obj.stderr.read().decode("GBK"))
