from socket import *
from threading import Thread, current_thread


def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

    while True:
        client.send(('%s say hello ' % current_thread().getName()).encode('utf-8'))  # io 不明显等待
        data = client.recv(1024)  # io 明显等待
        print(data.decode('utf-8'))

    client.close()


if __name__ == '__main__':
    for i in range(500):
        t = Thread(target=client)
        t.start()
