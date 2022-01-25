# 反射
# 可以通过字符串得形式来操作对象得属性

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking.....")


def talk(object):
    print("talking.....")


p = Person("Alex", 22)
if hasattr(p, "name"):  # 有name这个属性再往后执行，没有不执行
    print("l>......")
# 反射
# getattr() 获取值
a = getattr(p, "age")
print(a)

# hasattr() 有
user_command = input(">>:").strip()
if hasattr(p, user_command):
    func = getattr(p, user_command)
    func()
# setattr() 赋值
# static 属性
setattr(p, "sex", "Female")
print(p.sex)
# 方法
setattr(p, "speak", talk)  # 给实例绑定
p.speak(p)

setattr(Person, "sb", talk)  # 给类绑定
p.sb()
# delattr() 删除
delattr(p, "age")
# del p.age

# 如何反射文件中的属性或方法
print(__name__)  # __main__就代表模块本身，与self类似
if __name__ == "__main__":  # 只会在被别人的模块导入的时候发挥作用
    print("HHHHH")

    # __name__在当前模块主动执行的情况下
    # （不是被导入执行 即不是import导入的模块）等于__main__
    # 在被其他模块导入的时候执行为模块的文件名

import sys

# for k,v in sys.modules.items():
#     print(k,v)

# print(sys.modules["__main__"])
print(sys.modules[__name__])
mod = sys.modules[__name__]
if hasattr(mod, "p"):
    o = getattr(mod, "p")
    print(o)  # o的地址，也就是通过反射拿到的p的地址
    print(p)  # p的地址

