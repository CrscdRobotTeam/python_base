# 属性方法
# 把一个方法变成一个静态的属性（变量）
class Student(object):
    role = "Stu"

    def __init__(self, name):
        self.name = name

    @property  # 属性
    def fly(self):  # 执行一些动作，把方法变成属性一样调用
        print(self.name, " is flying")


s = Student("Tom")
# s.fly()#TypeError: 'NoneType' object is not callable
s.fly


# 只是调用方式发生改变，不能传值
# s.fly=1#AttributeError: can't set attribute

# 修改property的值
class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("connecting airline company api....")
        print("checking flight %s status " % self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("connot confirm the flight status ...,please check later")

    @flight_status.setter  # 修改
    def flight_status(self,status):
        status_dic = {0: "canceled", 1: "arrived", 2: "departured"}
        print("\033[31;1mHas changed the flight status to \033[0m", status_dic.get(status))
    @flight_status.deleter #删除
    def flight_status(self):
        print("del...")

f = Flight("CA980")
f.flight_status
f.flight_status = 2
del f.flight_status
