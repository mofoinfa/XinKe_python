# 家庭作业
# 1,创建一个py文件，里面有一些功能
# 2,里面要求有 加减乘除的函数方法  示例
# def add(a, b):
#     return a + b
# 3,是否可以被整除（%函数功能，可以就返回True 不行就返回False）
# 4,是否是奇偶数(奇数返回1 偶数返回2)
# 5,上面所有的判断传入的数据类型是否是数字（包含浮点），如果类型不对就抛出异常

from tool import func
a, b = input('请依次输入两个数据进行测试:').split()
try:
    a, b = float(a), float(b)
    print(f'加法结果:{func.add(a, b)}')
    print(f'减法结果:{func.delete(a, b)}')
    print(f'乘法结果:{func.ride(a, b)}')
    print(f'除法结果:{func.divide(a, b)}')
    print('是否可以整除:是') if func.exact_division(a, b) else print('是否可以整除:否')
    print(f"奇偶数判断：a({'奇数' if func.odevity(a) == 1 else '偶数'}),b({'奇数' if func.odevity(b) == 1 else '偶数'})")
except ValueError:
    print("传入的数据需要是数字")

# 所学内容
# 一、模块导入
# 1.第一种方法（导入整个模块）
from tkinter import *  # 很容易发生文件的冲突 不推荐使用的
# from PIL import *
# 2.第二种方法（导入整个模块）
# import tkinter  # 方便使用
# import PIL
# eg:以上两个调用模块均包含Image的类，利用以下的方法可以避免重复
# tkinter.Image，PIL.Image
# 3.第三种方法
# from tkinter import Image as tk_Image
# from PIL import Image as pil_Image
# 只tkinter的模块中中Image方法，并用as命名为tk_Image，利用名字直接调用方法
# tk_Image,pil_Image
# 优点：减少打包时占用的内存
# 4.导入路径
# 导入一个模块会先找 同级路径-》项目路径-》模块路径
# 系统文件 python\Lib
# 下载的文件 python\Lib\site-packages

# 二、模块下载
# 1.终端下载      pip install 模块的名字
# 2.删除         pip uninstall 模块的名字
# 3.设置下载版本   pip install 模块的名字==版本号
# 4.使用清华镜像源 pip install 模块名称 -i https://pypi.tuna.tsinghua.edu.cn/simple
# 5.升级         pip python -m pip install --upgrade pip

