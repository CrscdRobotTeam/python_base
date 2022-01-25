# call
# 对象后面加括号，触发执行。
# 注：构造方法new的执行是由创建对象触发的，
# 即：对象 = 类名() ；而对于 call 方法的执行是由对象后加括号触发的，
# 即：对象() 或者 类()()


class Person(object):
    def __init__(self, name):
        self.name = name
        print("--init ....")

    def __new__(cls, *args, **kwargs):
        """
        cls  : 代表Person这个类本身
        :param args:
        :param kwargs:
        :return:
        """
        print("--in new: ", cls, *args, **kwargs)

        return object.__new__(cls)  # 调用父类的__new__方法，必须这么干 ，要不然__init__方法就不会执行了

    def __call__(self, *args, **kwargs):
        print("-->call", self, *args, **kwargs)


p = Person("Alex")

p()  # 此时会执行__call__
Person("Alex")()