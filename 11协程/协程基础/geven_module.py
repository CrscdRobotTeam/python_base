# from gevent import monkey
#
# monkey.patch_all()  # 检测下面代码中所有IO操作 这次用time.sleep(32)也可自动切换
# import gevent
#
#
# def eat(name):
#     print('%s eat 1' % name)
#     gevent.sleep(2)  # 只能识别自己模块的io操作 用time.sleep(2)就变成串行执行的了 用monkey解决
#     print('%s eat 2' % name)
#
#
# def play(name):
#     print('%s play 1' % name)
#     gevent.sleep(1) #  用time.sleep(2)就变成串行执行的了 用monkey解决
#     print('%s play 2' % name)
#
#
# g1 = gevent.spawn(eat, 'egon')  # 异步提交，主线程结束，就结束
# g2 = gevent.spawn(play, name='elex')
#
# g1.join()  # 保证执行完再执行下面的代码
# g2.join()
# # 或者gevent.joinall([g1,g2])
# print('主')


from gevent import monkey

monkey.patch_all()  # 检测下面代码中所有IO操作 这次用time.sleep(32)也可自动切换
import gevent, time


def eat(name):
    print('%s eat 1' % name)
    time.sleep(2)  # 第二个io
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(1)  # 第三个io
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')  # 异步提交，主线程结束，就结束
g2 = gevent.spawn(play, name='elex')

#time.sleep(5)  # 三个任务切换 第一个io

#方法1:
# g1.join()  # 保证任务执行完完再执行下面的代码
# g2.join()

#方法2：
gevent.joinall([g1,g2])