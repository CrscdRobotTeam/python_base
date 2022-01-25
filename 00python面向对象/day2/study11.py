# 类的双下划线方法：
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):  # 必须返回一个整数，类默认没有，要用需要显示定义该方法

        print("trigger.....")
        return 2

    def __hash__(self):  # 类默认会有，不显示定义调用默认的，显示定义调用新定义的
        print("hash method.....")
        return hash(self.name + str(self.age))

    def __eq__(self, other):  # 类默认会有，不显示定义调用默认的，显示定义调用新定义的
        print(self.name, other.name)


p = Person("alex", 22)  # 调用__init__
print(len(p))  # 调用__len__
print(hash(p))
p1 = Person("jack", 22)
print(p == p1)


# item系列
# 可以把一个对象变成dict， 可以像dict一样增删改查
class Brand:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print("获取KEY", item)
        print(self.__dict__[item])

    def __setitem__(self, key, value):
        print("设置一个key...", key)
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('del obj[key]时,我执行')
        self.__dict__.pop(key)

    def __delattr__(self, item):  # del a.name
        print('del obj.key时,我执行')
        self.__dict__.pop(item)


b = Brand('小猿圈')
b["slogan"] = "自学编程谁不爱小猿圈"
b["website"] = "apeland.cn"

del b["website"]

b['name'] = '小猿圈Apeland'

b["name"]  # 获取KEY
print(b.__dict__)
