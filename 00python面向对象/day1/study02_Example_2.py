#多继承C3算法

class A:
    def test(self):
        print('from A')

class B(A):
    # def test(self):
    #     print('from B')
    pass

class B2:
    def test(self):
        print('from B2')

class C(A):
    def test(self):
        print('from C')

class C2:
    def test(self):
        print('from C2')

class D(B,B2):
    # def test(self):
    #     print('from D')
    pass

class E(C,C2):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass


f1=F()
f1.test()
print(F.__mro__) # 打印类的继承顺序