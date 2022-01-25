# 对象间交互
class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性是狗

    def __init__(self, name, breed, attack_val):
        self.name = name  # 每一只狗都有自己的名字
        self.breed = breed  # 每一只狗都有自己的品种
        self.attack_val = attack_val  # 每一只狗都有自己的攻击力
        self.life_val = 100  # 每一只狗都有自己的生命值

    def bite(self, person):
        # 狗可以咬人，这里传递进来的person也是一个对象。
        person.life_val -= self.attack_val  # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
        print("狗[%s]咬了人[%s],人掉血[%s],还剩血量[%s]..." % (self.name, person.name, self.attack_val, person.life_val))


class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.attack_val = attack_val
        self.life_val = 100
        self.sex = sex

    def attack(self, dog):
        # 人可以攻击狗，这里传递进来的dog也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_val -= self.attack_val
        print("人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s]..." % (self.name, dog.name, self.attack_val, dog.life_val))


d = Dog("妞妞", "哈士奇", 20)
p = Person("Alex", "Male", 60)

d.bite(p)
p.attack(d)


# 依赖关系
class Dog:
    def __init__(self, name, age, breed, master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master  # master传进来的应该是个对象
        self.sayhi()  # 调用自己的方法在实例化的时候

    def sayhi(self):
        print("Hi, I'm %s, a %s dog, my master is %s" % (self.name, self.breed, self.master.name))


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def walk_dog(self, dog_obj):
        # pass """遛狗"""
        print("主人[%s]带狗[%s]去溜溜。。。" % (self.name, dog_obj.name))


p = Person("Alex", 26, "Male")
d = Dog("Mjj", 5, "二哈", p)

p.walk_dog(d)


# 关联关系
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        # partner应该是一个对象
        self.partner = None  # 第一个person初始化的时候第二个人还没有，所以只能先置为空，都初始化后再绑定

    def do_private_stuff(self):
        pass


p1 = Person("Marry", 24, "M")
p2 = Person("Jhon", 23, "F")

# 双向关联
p1.partner = p2  # Jhon为Marry的partner
p2.partner = p1
print(p1.partner.name, p2.partner.name)

# 双向解除绑定
p1.partner = None
p2.partner = None
print(p1.partner, p2.partner)


class Person:
    def __init__(self, name, age, sex, relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation

    def do_private_stuff(self):
        pass


class RelationShip:
    """保存couple之间的对应关系"""

    def __init__(self):
        self.couple = []  # 初始化的时候可能还没有obj1,obj2，所以在初始化的时候赋值不太好

    def make_couple(self, obj1, obj2):
        self.couple = [obj1, obj2]
        print("[%s]和[%s]确定了关系..." % (obj1.name, obj2.name))

    def get_my_partner(self, obj):
        #print("找[%s]的相关人" % obj.name)
        for i in self.couple:
            if i != obj:
                return i
        else:
            print("没有与你有关系的人...")

    def break_up(self):
        print("[%s][%s]关系解除..."%(self.couple[0].name,self.couple[1].name))
        self.couple.clear()


relation_obj = RelationShip()  # 初始化
p1 = Person("Mira", 24, "M", relation_obj)
p2 = Person("Jason", 23, "F", relation_obj)

# 双向绑定
relation_obj.make_couple(p1, p2)
print(p1.relation.get_my_partner(p1).name)

#关系解除
p1.relation.break_up()
p2.relation.get_my_partner(p2)