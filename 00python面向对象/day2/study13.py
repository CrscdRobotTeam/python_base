# 异常处理 isinstance\issubclass

# isinstance(obj, cls)检查obj是否是类 cls 的对象
class Foo(object):
    pass


obj = Foo()

print(isinstance(obj, Foo)) # 判断实例obj是不是Foo产生的，是返回True

# issubclass(sub,super)检查sub类是否是 super 类的派生类

class Foo(object):
    pass

class Bar(Foo):
    pass

print(issubclass(Bar, Foo))