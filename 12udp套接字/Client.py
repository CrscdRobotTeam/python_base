# udp是数据报协议，带端口信息，可以发数据空
# udp不会粘包，单独数据就是一个完整的数据包
# 没有管道，收不完就丢失
from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>:').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
    data, server_addr = client.recvfrom(1024)
    print(data, server_addr)

client.close()
