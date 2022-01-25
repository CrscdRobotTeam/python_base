# new方法，单例模式就用new来写
# 我们知道实例化init会自动执行， 其实在init方法之前，还有一个new方法也会自动执行，
# 你可以在new里执行一些实例化前的定制动作
class Printer(object):
    __instance = None  # 用来存唯一的一个实例
    __tasks = []

    def __init__(self, task):
        self.__tasks.append(task)
        print("added a new task in queue..", task)

    def __new__(cls, *args, **kwargs):  # 负责执行__init__
        if cls.__instance is None:  # 代表之前还没被实例化过
            obj = object.__new__(cls)  # 执行init
            cls.__instance = obj  # 把第一次实例化的对象 存下来，以后每次实例化都用这个第一次的对象
        return cls.__instance  # 下一次实例化时，就返回第一次实例化的对象

    def jobs(self):
        return self.__tasks


job = Printer("job1 word")
job2 = Printer("job2 png")
job3 = Printer("job3 excel")
print(id(job), id(job2), id(job3))  # 会发现这3个实例的内存id一样
print(job3.jobs())
