# 家庭作业 用递归求5的阶乘（5x4x3x2x1）
# def get_data(num):
#     if num == 1:
#         return 1
#     else:
#         return num * get_data(num - 1)
#
#
# print(get_data(5))

# 所学内容
# 一、递归
# 定义：重复调用自身的函数
# 例题1 使用递归算法输出1-9
# def print_num(start, stop):
#     if start == stop:
#         print(start)
#         return
#     else:
#         print(start)
#         return print_num(start + 1, stop)
#
#
# print_num(1, 9)
# 例题2  按照顺序输出list_data = [1, [2, 3, [4, 5, 6, [7, 8, 9, [0]]]]](按照1-9进行输出)
# def print_num(list_data):
#     for i in list_data:
#         if isinstance(i, list):
#             print_num(i)
#         else:
#             print(i)
#
#
# list_data = [1, [2, 3, [4, 5, 6, [7, 8, 9, [0]]]]]
#
# print_num(list_data)

# 二、lambda 的应用
# 定义：匿名函数
# 1.
# 只调用一次
# (lambda b: b + b)(1)
# 2.
# 调用多次
# add = lambda a, b: a + b  ##a,b为传入的参数，a+b为返回的值
# print(add(1, 2))

# 三、高阶函数的应用
# 1.map 映射
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map(函数名，可迭代对象)
# 定义：可迭代对象向函数内按照顺序依次传入一个值，函数名不用带括号，最后返回一个对象
# print(list(map(str, list1)))  # 生成器对象
# 2.reduce
# 定义：可迭代对象向函数内按照顺序依次传入两个值，函数名不用带括号，最后返回一个对象
# from functools import reduce  # from 从什么地方  import 导入什么东西
#
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(reduce(lambda a, b: a + b, list2))
#
# 大致流程：
# 1   2     3     4
# a + b =
#       a + b =
#             a + b