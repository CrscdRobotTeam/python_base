import codecs
import itertools
import math
from array import array
from datetime import datetime, timedelta, date
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='cau', database='patroldb_newmap')
# 创建游标
# cursor = conn.cursor()
# 定制游标 拿出数据成字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# name = input('请输入名字：>>').strip()
# age = input('请输入年龄：>>').strip()
# 不用字符串格式化得方式
# sql='insert into student (name,age) values("%s",%s)'%('lily or 1=1 -- ',age)
# l_tup = [
#
#     ('Lily0', 3),
#     ('Lily1', 4),
#     ('Lily2', 5)
# ]
# result返回受影响条数
# result = cursor.execute(sql)  # 执行SQL语句
# result = cursor.execute('insert into student (name,age) values(%s,%s)', (name, age))
# result = cursor.executemany('insert into student (name,age) values(%s,%s)', l_tup) # 等同于下一语句
# result = cursor.executemany('insert into student (name,age) values(%s,%s)', [('Lily0', 3),('Lily1', 3),('Lily2', 3)])
# result = cursor.execute('update student set name=%s where name=%s', ('lily', 'Lily0'))
# result = cursor.execute('delete from student where name=%s', 'lily')
# 增加、删除、修改用commit，查不用
# conn.commit()
# print(result)
# r返回受影响条数
# r = cursor.execute('select * from student')  # 执行完此条，数据已经从数据库拿到内存中
# re = cursor.execute('select planname as n,2020-06-10 as i from taskplan')
# task = '计划'
# # re = cursor.execute('select planname as name from taskplan where planname=%s limit 1',task)
#
# result = cursor.execute(
#     'select planStartDate,planTime as starttime, planEndTime as endtime,planStatus as status from taskplan order by planTime asc')
# # # re从内存中取出元组
# re = cursor.fetchall()  # 获取所有记录列表
# print(re)

result = cursor.execute(
                'select planName, planStartTime,planEndTime,planDevNum,planDevNum,planErrDevNum,planCheckOrder\
                 from planstorage order by id asc')
getId = cursor.fetchall()
if result > 0:
    print({"info":1,"id":getId})
# # re = cursor.fetchmany(3)  # 拿几条数据3改成几
# # re = cursor.fetchone()  # 取一条数据
# cursor.execute('select * from taskplan')
# result = cursor.fetchall()
# print(result)
# nodelist = [0, 6, 7, 8]
# arr = []
# for item in nodelist:
#     result = cursor.execute('select robotX,robotY from map2dcruxponit where id=%s', (item))
#     getRoute = cursor.fetchone()
#     if result == 1:
#         arr.append([getRoute['robotX'], getRoute['robotY']])
# print(len(arr))
# print(arr)
# a = arr
# print(a)
# list = []
# list.append(1)
# print(list.clear())
# print(len(list))
# print({'result': result, 'info': list})
# # for row in re:
# #     fname = row[0]
# #     # 打印结果
# #     print("fname=%s" % (fname))
# print('---------------------')
# print(len(re))
# for item in re:
#     print(item['starttime'])
# 获取最新自增ID

# taskInfo = {'planName': '第3次测试', 'taskTemp': 17, 'planStartDate': '2020-06-30', 'planTime': datetime.strptime('23:10:20', '%H:%M:%S'),
#         'planEndTime': datetime.strptime('23:28:20', '%H:%M:%S'), 'planEndDate': '2020-06-20', 'RepType': 0, 'RepTime': 0, 'planStart': 1,
#         'planStatus': 0}
# #datetime.strptime('23:28:20', '%H:%M:%S').strftime('%H:%M:%S')
# result =cursor.execute(
#     'insert into taskplan (planName,taskTemp,planStartDate,planTime,planEndTime,planEndDate,RepType,\
#     RepTime,planStart,planStatus) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
#     (taskInfo['planName'], taskInfo['taskTemp'], taskInfo['planStartDate'], taskInfo['planTime'],
#      taskInfo['planEndTime'], taskInfo['planEndDate'], taskInfo['RepType'], taskInfo['RepTime'],
#      taskInfo['planStart'], taskInfo['planStatus']))
# conn.commit()
# print(result)
# item = {'name': '电力变压器', 'subClassName': '3BX', 'pointName': '3Bx1'}
# cursor.execute('select id from devicetype where name=%s', (item['name']))
# deviceId = cursor.fetchone()
# print(deviceId)
# cursor.execute('select id from devicesubclass where subClassName=%s and deviceId=%s',
#                (item['subClassName'], deviceId['id']))
# deviceSubclassID = cursor.fetchone()
# print(deviceSubclassID)
# result = cursor.execute(
#     'select checkPointId from patroldevice where pointName=%s and deviceSubClassID=%s and deviceId=%s',
#     (item['pointName'], deviceSubclassID['id'], deviceId['id']))
# print(result)
# checkPointId = cursor.fetchall()
# print(checkPointId)

# print('----------------------------------------')
# new_id = cursor.lastrowid
# print(new_id)

# cursor.close()
# conn.close()

# mysqlconf = {'host': 'localhost', 'user': 'root', 'pw': 'cau', 'db': 'patroldb_newmap'}
# a, b, c, d = mysqlconf['host'], mysqlconf['user'], mysqlconf['pw'], mysqlconf['db']
# print(type(a))
# print('a=%s b=%s c=%s d=%s' % (a, b, c, d))

'''

# print(time.strftime("%Y%m%d %H%M%S",time.localtime()))

print((datetime.min + re[0]['time']).time().strftime('%H%M%S'))
print(str(re[0]['date'].year) + str(re[0]['date'].month) + str(re[0]['date'].day))
import operator as op

print(op.lt(datetime.now().strftime('%Y%m%d%H%M%S'),
            (re[0]['date'].strftime('%Y%m%d') + (datetime.min + re[0]['time']).time().strftime('%H%M%S'))))


plandate = '2020-02-02'
plantime = '20:02:12'
starttime = time.strftime('%Y%m%d %H%M%S', time.strptime(plandate + ' ' + plantime, '%Y-%m-%d %H:%M:%S'))
print(starttime)
'''

# import time
#
# # str--datetime
# print(type(datetime.strptime('201636', '%Y%m%d')))
# print(datetime.strptime('23:13:13',  '%H:%M:%S')-datetime.strptime('20:10:59',  '%H:%M:%S'))
# print(type(datetime.strptime('2016-06-07', '%Y-%m-%d')))
# print(datetime.date(datetime.strptime('2016-12-30', '%Y-%m-%d')))
# print(timedelta(seconds=361))
# print(datetime.now() + timedelta(seconds=361))
# print(time.strftime('%Y%m%d', time.strptime('2020-06-25', '%Y-%m-%d')) + ' ' + time.strftime('%H%M%S',
#                                                                                              time.strptime('08:59:20',
#                                                                                                            '%H:%M:%S')))
#
#
# def ti():
#     print(type(time.strptime('080903', '%H:%M:%S')))
#
#
# try:
#     ti()
# except:
#     print('AAAA')
# a={'a':1,'b':2,'c':3}
#
# b={'d':4,'e':5,'f':6}
#
# print(dict(a,**b))
#
# from dateutil import relativedelta
# print(datetime.strptime('2020-12-02 08:09:10','%Y-%m-%d %H:%M:%S') + relativedelta.relativedelta(months=2))
# print(timedelta(seconds=100/2))
# print(datetime.strptime('2020-06-25 20:10:59', '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'))
# print(date(2020, 7, 18) > date(2020,
# 8, 12))
# print(math.ceil(1194.002 / 100))
# print(timedelta(seconds=12*60))
# l = [{"a":1},{"a":2},{"a":3}]
# print(l[len(l)-1]["a"])
#
# m = ()
# for i in m:
#     print(i)
print(datetime.strptime('2020-02-01 08:09:10','%Y-%m-%d %H:%M:%S')+ timedelta(days=3+1))
# l = [1,1,2,3,5,7,1,2,1]
#
# for i in range(len(l)-1,-1,-1): # 倒序循环，从最后一个元素循环到第一个元素。不能用正序循环，因为正序循环删除元素后后续的列表的长度和元素下标同时也跟着变了，len(alist)是动态的。
#     if l[i] == 1:
#         l.pop(i) # 将index=i处的元素删除并return该元素。如果不想保存这个被删除的值只要不把alist.pop(i)赋值给变量就好，不影响程序运行。
#
# print(l) # [7, 4, 2, 1]

print(datetime.strptime('2020-01-01 08:09:10','%Y-%m-%d %H:%M:%S') > datetime.strptime('2020-02-01 08:09:00','%Y-%m-%d %H:%M:%S'))

# print(("1" or "12")in"12,2,3".split(","))
# a=[]
#
# a.sort()
# print(a)
# print(datetime.now().isoweekday())
# print(type(datetime.now().isoweekday()))
# print(date.today() - timedelta(days=(8-datetime.now().isoweekday())))
# print(datetime.strptime('2020-02-01 08:09','%Y-%m-%d %H:%M'))
# print(datetime.strptime(date.today().strftime(),'%Y-%m-%d'))
print(datetime.strptime('2020-01-01 08:09:10','%Y-%m-%d %H:%M:%S')+timedelta(seconds=361))


def str_to_hex(s):
    return '\\'.join([hex(ord(c))for c in s])
print(len('2020-10-20 08:10:24|19|20|22'))
print(type(str_to_hex("2020-10-20 08:10:24|19|20|22")))
arr=bytearray()
for item in "我吧||ff99a":
    print("-----------------------------")
    if len(hex(ord(item)))>4:

        arr.append(int(hex(ord(item))[0:4],16))
        print(int(hex(ord(item))[0:4],16))
        arr.append(int("0x"+hex(ord(item))[4:],16))
        print(int("0x"+hex(ord(item))[4:],16))
    else:
        arr.append(int(hex(ord(item))[0:4], 16))
import struct
print(len(struct.pack('!i', 254 + 1)))
print(type(struct.pack('!i', 254 + 1)))
print(struct.pack('!i', 257 + 1))
print(struct.pack('!i', 254 + 1)[3])
print("hex-type",type(hex(struct.pack('!i', 254 + 1)[3])))
print("120-102 12e"+'|'+str(1))
print(date.today().strftime('%Y-%m-%d'))
data="2020-10-29 12 123"

print(len("我们的||a"))
print(hex(ord("|")))
print(type(hex(eval("0xfc"))))


import binascii
arr.append(50)
arr.append(0xff)
arr.append(0x60)
print(arr)


print(hex(struct.pack('!i', 288 + 1)[2]))
print(hex(struct.pack('!i', 288 + 1)[3]))
brr=bytearray("我们2020 ： - |80|12","utf-8")
arr.extend(brr)
print(arr)
print(ord("我"))
print(ord("2"))
print(hex(ord("|")))
print(hex(54))
print(hex(61))

print(type({"error":1}))
print(type({}))
print(type({"error":1})==type({}))

print(datetime.strptime('20:09','%H:%M').strftime('%H:%M:%S'))

print((datetime.strptime("08:09:07","%H:%M:%S")+timedelta(seconds=3600)).strftime('%H:%M:%S'))
print(type(timedelta(seconds=3600)+timedelta(minutes=10)))


# task={'planName': '0007', 'taskTemp': 108, 'planStartDate': '2020-08-31', 'planTime': '17:00:41', 'planEndTime': '17:04:04', 'planEndDate': '2020-08-31', 'RepType': 0, 'RepTime': 0, 'planStart': 1, 'planStatus': 0}
# result = cursor.execute(
#     'insert into taskplan (planName,taskTemp,planStartDate,planTime,planEndTime,planEndDate,RepType,\
#     RepTime,planStart,planStatus,downloadCode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
#         task['planName'], task['taskTemp'], task['planStartDate'], task['planTime'], task['planEndTime'],
#         task['planEndDate'], task['RepType'], task['RepTime'], task['planStart'], task['planStatus'],
#         task['downloadCode']))
# conn.commit()
# print(result)

cursor.execute('select * from planstorage')
result = cursor.fetchall()
print(result)

print((result[0]['planStartTime']).strftime('%Y-%m-%d %H:%M:%S'))
plan=['wo','ai']
print({plan[0]:1})
index=1
print(["seq[%s]"%index,1])

field = {
    'name': "paramrlt",
    'code': "paramrlt",
    'subName': '固安东变电所',
    'startTime': "paramrlt",
    'endTime': "paramrlt",
}
field=dict(field, **{"a":1})
print("field=",field)
print(len({}))
print(len({"a":1,"b":2}))

result = cursor.execute('delete from taskplan  where id=%s', (135))
conn.commit()
print("__________________________")
print(cursor.lastrowid)
cursor.close()
conn.close()