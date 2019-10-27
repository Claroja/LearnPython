from .Module1 import *  # 模块之间的导入对于包来说需要用相对路径

print(module1)
module2 = 2

if __name__ == "__main__":
    from importmodule import Module1  # 主程序应用既__main__,需要使用包名来导入
    print(Module1.module1)