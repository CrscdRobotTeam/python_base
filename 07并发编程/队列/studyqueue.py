from multiprocessing import Process,Queue
#一个进程放数据另外一线程取数据 文件名不能叫queue
q = Queue(3)
''' 
队列里不放大文件，只为了进程间通讯，开辟的一块共享内存
进程将一条消息放大队列，另外一个进程取，
所以队列中的数据应该为小数据
'''
'''
队列可以不指定大小，意味着可以往里面放无穷无尽的数据，
但是队列用的是内存
'''
q.put('hello')
q.put({'a': 1})  # 字典
q.put([3, 3, 3,])  # 列表


#put ,get ,put_nowait,get_nowait,full,empty

print(q.full()) #满了
# q.put(4) #再放就阻塞住了,卡住

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了
# print(q.get()) #再取就阻塞住了 卡住