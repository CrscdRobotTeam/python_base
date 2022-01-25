# 继承
class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("%s is eating ..." % self.name)


class Person(Animal):  # 加括号为继承
    pass


class Dog(Animal):
    pass


p = Person("lily", 23, "M")
p.eat()
print(p.a_type)

d = Dog("mii", 4, "F")
d.eat()
d.a_type = "低等生物"
print(d.a_type)


class Person(Animal):  # 加括号为继承

    def talk(self):  # 新方法
        print("person %s is talking...." % self.name)

    def eat(self):  # 扩展父类的方法
        Animal.eat(self)  # 先执行父类的方法,不写此局直接执行子类方法
        print("%s 在优雅地吃....." % self.name)


p1 = Person("CoCo", 2, "M")
p1.talk()
p1.eat()


class Person(Animal):  # 加括号为继承

    def __init__(self, name):  # 覆盖父类初始化
        self.name = name

    def talk(self):  # 新方法
        print("person %s is talking...." % self.name)

    def eat(self):  # 扩展父类的方法
        # Animal.eat(self)  # 先执行父类的方法,不写此局直接执行子类方法
        print("%s 在优雅地吃....." % self.name)


p = Person("Mira")
p.eat()


class Person(Animal):  # 加括号为继承

    def __init__(self, name, age, sex, hobby):  # 覆盖父类初始化
        # Animal.__init__(self, name, age, sex) #写法1
        # super(Person, self).__init__(name, age, sex)  # py3写法2
        super().__init__(name, age, sex)  # 写法3
        self.hobby = hobby
        print("%s的爱好是%s" % (self.name, self.hobby))

    def talk(self):  # 新方法
        print("person %s is talking...." % self.name)

    def eat(self):  # 扩展父类的方法
        # Animal.eat(self)  # 先执行父类的方法,不写此局直接执行子类方法
        super(Person, self).eat(self)  # 执行父类方法，多继承时，按照顺序继承
        print("%s 在优雅地吃....." % self.name)


p2 = Person("Mali", 23, "M", "唱歌")
