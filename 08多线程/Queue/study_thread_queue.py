import queue

q = queue.Queue(3)  # 先进先出

q.put('first')
q.put(2)
q.put('third')
# q.put(4)#最大空间3，放四个阻塞，卡在原地
# q.put(4, block=True, timeout=3)
# 默认为阻塞，超时时间为3，超过时间还在阻塞，报错
# block=False 超过数量直接报错
print(q.get())
print(q.get())
print(q.get())
# print(q.get())#最大数量为3，取四个，卡在原地
# print(q.get(block=True, timeout=3)) # 等同于q.put_nowait()
## 默认为阻塞，超时时间为3，超过时间还在阻塞，报错
# block=False 超过数量直接报错
#print(q.get_nowait())  # 等同于block=False

#q = queue.LifoQueue(3)  # 后进先出--堆栈

q = queue.PriorityQueue(3)  # 优先队列

q.put((10,'one'))
q.put((40,'two'))
q.put((30,'three'))

print(q.get())
print(q.get())
print(q.get())
'''数字越小优先级越高'''