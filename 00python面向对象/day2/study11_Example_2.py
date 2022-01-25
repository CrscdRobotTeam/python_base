# del 析构方法
# 析构方法，当对象在内存中被释放时，自动触发执行。
class Foo:

    def __del__(self):
        print('执行我啦')

f1=Foo()
del f1
print('------->')


