import socket
import time

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(("127.0.0.1", 8080))

# 两个包,数据量小，时间间隔短
phone.send("hello".encode("GBK"))
time.sleep(5)#5s
phone.send("word".encode("GBK"))

phone.close()
