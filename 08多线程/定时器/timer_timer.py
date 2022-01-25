# from threading import Timer
#
#
# def task(name):
#     print('hello %s ' % name)
#
# t = Timer(5,task,args=('egon',))
# t.start()
## print(make_code(4))
# print(make_code())


from threading import Timer
import random


class code():
    def __init__(self):
        self.make_catch()

    def make_catch(self, interval=10):
        self.catche = self.make_code()  # 最开始拿到一个码
        print(self.catche)
        '''定时产生一个新的码 用定时器'''
        self.t = Timer(interval, self.make_catch)
        self.t.start()

    def make_code(self, n=4):
        res = ''
        for i in range(n):
            s1 = str(random.randint(0, 9))  # 产生0-9数字，转化为字符str
            s2 = chr(random.randint(65, 90))  # 产生a-z的ASCII码，转化为字母
            res += random.choice([s1, s2])  # 随机选择一个
        return res

    def check(self):
        while True:
            code = input('请输入验证码>>:').strip()
            if code.upper() == self.catche:
                print('验证码输入正确')
                self.t.cancel()
                break


obj = code()
obj.check()
