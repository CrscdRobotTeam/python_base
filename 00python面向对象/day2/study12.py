# 用type动态创建一个类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alex", 22)
print(type(p))  # 输出 p的父类
print(type(Person))  # 输出


# p对象是Person类的一个实例，Person类对象是 type 类的一个实例，
# 即：Person类对象 是通过type类的构造方法创建。
def __init__(self, name, age):
    self.age = age


dog_class = type("Dog", (object,), {"role": "dog","__init__":__init__})
# type("类名",(继承于1,继承于2...),{"属性":"属性值","方法名"：方法})
print(dog_class)
d = dog_class("mjj",3) # 实例化
print(d.role)
print(d.name)
