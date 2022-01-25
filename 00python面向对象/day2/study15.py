# 断言
# assert语法用于判断代码是否符合执行预期


assert type(1) is int
assert 1 + 1 == 2
# assert 1 + 1 == 3  # 会报AssertionError

# 应用场景举例，别人调你的接口，你的接口要求他调用时必须传递指定的关键参数，
# 等他传递进来时，你就可以用用assert语句他传的参数是否符合你的预期


def my_interface(name,age,score):
    assert type(name) is str
    assert type(age) is int
    assert type(score) is float

my_interface("alex",22,89.2)