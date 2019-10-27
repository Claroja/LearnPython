"""
global关键字在方法面声明，声明之后该变量从方法的局部变量变成模块的全局变量（相当于在模块里命名了一个全局变量）
1. global只是将该变量的作用域从方法提升到该模块(如果有其他模块调用该模块，其他模块不共享该变量）
2. 必须先调用声明global变量的方法，否则会报出变量未定义的错误.比如先调用test2()，再调用test1()
"""




def test1():
    global a
    a=2
    print("test1:%s"%a)


def test2():
    print("test2:%s"%a)  # 直接调用global变量a


if __name__ == "__Main__":
    test1()
    test2()
