# 封装

class Person(object):
    def __init__(self, name, age):
        self.name = name  # 实例变量、成员变量
        self.age = age
        self.__life_val = 100  # 私有变量，外面访问不了，前面两个下划线
        self.__breath()

    def get_life_val(self):  # 只读
        print("生命值还有 ", self.__life_val)
        return self.__life_val

    def got_attack(self):
        self.__life_val -= 20
        print("被攻击，生命值还剩", self.__life_val)
        return self.__life_val

    def __breath(self):  # 私有方法，内部调用
        print("%s 在呼吸" % self.name)


p = Person("lily", 7)
print(p.name)
p.get_life_val()
p.got_attack()

# 访问私有函数
p._Person__breath()
p._Person__life_val = 10
p.get_life_val()

p.__def = 333  # 实力生成后，在外面创建得变量有__也不是私有属性
print(p.__def)
