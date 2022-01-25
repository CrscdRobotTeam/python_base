# 异常处理
# 把可能会发生的错误，提前在代码里进行捕捉（检测）
# try:
#       your code
# except Exception: # 万能错误，可以抓取所错误
#       出错后执行的代码

# 自定义异常
class MyException(BaseException): # BaseException是所有异常的基类
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

# try:
#     raise MyException("我的错误")
#
# except MyException as e:
#     print(e)

while True:
    try:
        num1 = int(input("n1>>: "))
        num2 = int(input("n2>>: "))

        res = num1 + num2

        print("result:", res)
        raise MyException("错误")  # 主动触发异常
    except MyException as e:
        print("MyException",e)
    except AttributeError as e:
        print(e)
    except (NameError, ValueError) as e:  # 多个错误
        print(e)
    except ValueError as e:
        print(e)
    except Exception as err:
        print(err)

        # 缩进错误IndentationError---捕捉不到---强类型错误
        # 语法错误SystaxError---捕捉不到---强类型错误

    else:  # 代码没发生异常
        print("没异常")
    finally:
        print("不管有没有发生异常都走这里")




