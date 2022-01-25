import struct

# res = struct.pack("i", 1280)  # 打包成固定长度的报文(i指的是int类型，有大小限制）
# print(res, type(res), len(res))
#
# # client.recv(4)
# obj = struct.unpack("i", res)  # 解包,返回元组
# print(obj, obj[0])  # 第一个元素就是数据

res = struct.pack("d", 11122222222222)  # long类型
print(res,len(res))
