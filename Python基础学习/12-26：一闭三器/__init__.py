# 家庭作业
# 创建一个获取代码运行所需时间的装饰器
import time


def func(f):
    def inter():
        start = time.time()
        print(f'函数结果:{f()}')
        stop = time.time()
        return stop - start

    return inter


@func
def add():
    t = 0
    for i in range(100000000):
        t += i
    return t


print(f'所需时间:{add()}')

# 所学内容
# 一、迭代器
# 1.判断对象是否可迭代
# print([1, 2, 3].__dir__())#查看里面所有的魔法方法，如果有__iter__，则此对象为可迭代对象
# 2.利用魔法方法进行对象的迭代输出
# print([1, 2, 3].__iter__().__dir__())  # 查看迭代对象的所有魔法方法
# data = [1, 2, 3].__iter__()#将迭代数据最为对象，依次输出下一个
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())

# 二、生成器
# 1.定义：一个特殊的迭代器，节省内存，把一个函数变成生成器，返回数据，并且不杀死函数
# 2.例题：取一个无限大的数字，并且使内存空间只为1
# def func():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
# data = func()
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())

# 三、闭包
# 1.定义：在一个函数内部又调用一个函数，保证数据的安全，函数运行完成，公共数据不会死亡
# 2.例题，不断调用函数，不断加入一个数字，依次输出列表
# def func():
#     list2 = [1]
#
#
#     def inner():
#         list2.append(len(list2)+1)
#
#         return list2
#
#     return inner
#
#
# inner = func()
#
# print(inner())
# print(inner())
# print(inner())

# 四、装饰器
# 1.作用
# （1）在不改变函数源码代码的同时为函数增加新的功能
# （2）减少重复的功能代码
# （3）设置缓存
# （4）不断计算代码的执行时间
# 2.例题，创建一个获取代码运行所需时间的装饰器
import time


def func(f):
    def inter():
        start = time.time()
        print(f'函数结果:{f()}')
        stop = time.time()
        return stop - start

    return inter


@func#等同于 add = func(add)
def add():
    t = 0
    for i in range(100000000):
        t += i
    return t


print(f'所需时间:{add()}')