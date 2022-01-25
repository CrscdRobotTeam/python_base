# 类方法、静态方法
# 类方法通过@classmethod装饰器实现，
#
# 类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量

class Dog(object):
    d_type = "金毛"  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量

    @classmethod
    def eat(cls):
        print("---", cls)  # cls是类本身,不能访问实例的变量
        print("%s is eating" % cls.d_type)


d = Dog("LL")
d.eat()


# class __main__.Dog 类本身
# --- <__main__.Dog object at 0x00000264B4C44288> 实例本身
# 存在公共的空间，类中

class Student(object):
    stu_num = 0

    def __init__(self, name):
        self.name = name
        self.stu_num += 1  # 给实例进行赋值
        print("新生成一个学生", name)


s = Student("美妞")
s1 = Student("花枝")
print(s.stu_num)


class Student(object):
    __stu_num = 0

    def __init__(self, name):
        self.name = name
        # Student.stu_num += 1  # 对类变量进行赋值
        # print("新生成一个学生", name)
        self.add_stu()

    @classmethod
    def add_stu(cls):
        cls.__stu_num += 1
        print("新生成一个学生", cls.__stu_num)


s = Student("美妞")
s1 = Student("花枝")

Student.add_stu()  # 从外面调用


class Student(object):
    __stu_num = 0

    def __init__(self, name):
        self.name = name
        # Student.stu_num += 1  # 对类变量进行赋值
        # print("新生成一个学生", name)
        self.add_stu(self)

    @classmethod
    def add_stu(cls, obj):  # obj stands for self instance
        if obj.name:
            cls.__stu_num += 1
            print("新生成一个学生", cls.__stu_num)


s = Student("美妞")
s1 = Student("花枝")

#Student.add_stu(Student)  # 从外面调用,不能直接调用
