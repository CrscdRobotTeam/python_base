class Dog:  # 类 或Dog():大驼峰式命名
    # 公共属性d_type
    d_type = "京巴"  # 属性，类属性，类变量 公共属性，所有实例共享Dog.d_type可调用

    # 初始化的时候传递一些不一样的数据，参数在实例化的时候直接传
    def __init__(self, name, age):  # 初始化方法，构造方法，构造函数，实例化时进行一些初始化工作，会自动执行,
        #self.d_type = name
        # 实例属性 name,age
        print("hahahha", name, age)  # 方法调用完，name和age就消失了
        # 想把name和age存下来，存到实例里，就要跟实例绑定,存到实例的内存空间
        self.name11 = name  # 绑定参数值到实例上，相当于 d1.name = name
        self.age11 = age  # 实例属性 不能用Dog.age调用

    def say_hi(self):  # 方法 self代表实例本身... 方法的第一个参数必须是self
        print("Hello ,i am a dog ,my type is ", self.d_type, self.name11, self.age11)  # 此时可以嗲用name和age


d = Dog("lelel", 2)  # 实例化：生成了一个实例，实例化的时候自动调用—__init__(self)方法
d.say_hi()  # 实例.方法
print(d.name11)  #实例.属性
print(id(d.d_type),id(Dog.d_type))  # 查看变量的内存空间，两个属性在同一个内存地址

d.gender = "F"# 实例属性，实例自己有的
print(d.gender)

# 类自己有一个内存空间，每个实例也有自己的内存空间
d.d_type = "金毛"#相当于d给自己创建了一个新实例属性，与原本的Dog.d_type无关
print(d.d_type,Dog.d_type)

Dog.d_type ="哈士奇"
print(d.d_type,Dog.d_type)#调用的时候先引用自己的属性

print(id(d.d_type),id(Dog.d_type))

# 代码选中的条件下，同时按住 Ctrl+/，被选中行被注释，再次按下Ctrl+/，注释被取消
# 快捷键组合是： Ctrl + Alt + L

