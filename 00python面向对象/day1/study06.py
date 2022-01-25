# 静态方法
# 不能访问 类 变量和方法，也不能访问 实例 变量和方法
class Student(object):
    role = "Stu"

    def __init__(self, name):
        self.name = name

    @staticmethod  # 割断了类和实例的任何关系
    def fly(self):
        print(self.name, " is flying")


s = Student("Tom")
# s.fly()  # ypeError: fly() missing 1 required positional argument: 'self'
s.fly(s)  # 不自动传s
