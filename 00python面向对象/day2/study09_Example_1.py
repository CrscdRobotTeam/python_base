# 反射的应用
class User(object):
    def login(self):
        print("欢迎来到登录界面")

    def register(self):
        print("欢迎来到注册界面")

    def save(self):
        print("欢迎来到存储界面")


u = User()
while True:
    user_cmd = input(">>:").strip()
    if hasattr(u, user_cmd):
        func = getattr(u, user_cmd)
        func()
