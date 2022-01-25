# 多态( Polymorphism )

class Dog(object):
    def sound(self):
        print("汪汪汪.....")


class Cat(object):
    def sound(self):
        print("喵喵喵.....")


def make_sound(animal_obj):
    """统一调用接口"""
    animal_obj.sound()  # 不管你传进来是什么动物，我都调用sound()方法


dogObj = Dog()
catObj = Cat()

make_sound(dogObj)
make_sound(catObj)


# 抽象类实现多态
class Document:  # 抽象类，必须重写show()方法
    def __init__(self, name):
        self.name = name

    def show(self):
        # raise抛出错误  NotImplementedError未执行的error
        raise NotImplementedError("Subclass must implement abstract method")  # 异常处理


class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'


class Word(Document):
    def show(self):  # 直接调用父类的报错
        return 'Show word contents!'


documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3')]

for document in documents:
    print(document.name + ': ' + document.show())
