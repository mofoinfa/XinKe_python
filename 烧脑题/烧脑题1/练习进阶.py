# # 1.1
# # 我们都知道：1+2+3+ ... + 49 = 1225。现在要求你把其中两个不相邻的加号变成乘号， 使得结果为 2015。
# # 例如： 1+2+3+...+10*11+12+...+27*28+29+...+49 = 2015 就是符合要求的答案。
# # 请你寻找所有可能的答案，并把前面的两个数字输出，如上面的就是输出（10 27）
# #
# sum_num = 0
# first_num = 0
# second_num = 0
# for i in range(1, 50):
#     for j in range(i + 1, 50):
#         for k in range(1, 50):
#             if i == k:  # 第一个乘数
#                 sum_num = sum_num + k * (k + 1)
#                 first_num = i
#             elif j == k:  # 第二个乘数
#                 sum_num = sum_num + k * (k + 1)
#                 second_num = j
#             else:
#                 if k == i + 1 or k == j + 1:
#                     continue
#                 else:
#                     sum_num += k
#         if sum_num == 2015 and second_num - first_num != 1:
#             print(first_num, second_num)
#         sum_num = 0
# # 1.2
# # 输入一个整数 n，计算并输出他的阶乘。
# # 注意：定义一个函数(或方法)，用于求阶乘的值。
# # 在主函数(或主方法)中调用该递归函数(或方法)，求出 5 的阶乘，并输出结果。
# #
# def get_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return get_factorial(n - 1) * n
#
#
# if __name__ == '__main__':
#     n = int(input('请输入整数n:'))
#     print(get_factorial(n))
#     print(f'5的阶乘{get_factorial(5)}')

# 简化版
# def get_factorial(n):
#     return 1 if n == 1 else get_factorial(n - 1) * n
#
#
# if __name__ == '__main__':
#     n = int(input('请输入整数n:'))
#     print(get_factorial(n))
#     print(f'5的阶乘{get_factorial(5)}')

# # 1.3
# # 由于中国结的形状是菱形图案，所以现在公司需要设计一个打印菱形的方法。从键盘输入一个整数 N，打印出有 N*2-1 行的菱形。
# # 例如输入整数 4，则屏幕输出如下菱形。
# #    *
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *
# # 现要求输入整数为 7，在屏幕中输出相应的菱形。要求：用循环结构语句实现。
# n = int(input('请输入整数n:'))
# # 输出上半部分
# for i in range(n):
#     for j in range(n - i):
#         print(' ', end='')
#     for j in range(1 + 2 * i):
#         print('*', end='')
#     print()
# # 输出下半部分
# for i in range(1, n):
#     for j in range(i + 1):
#         print(' ', end='')
#     for j in range(1 + 2 * (n - i - 1)):
#         print('*', end='')
#     print()
#
#
# # 1.4
# # 编写程序输出 2~99 之间的同构数。同构数是指这个数为该数平方的尾数，例如 5 的平方为 25，6 的平方为 36，25
# # 的平方为 625，则 5、6、25 都为同构数。
# # 注意：调用带有一个输入参数的函数(或方法)实现，此函数(或方法)用于判断某个整数是否为同构数，
# # 输入参数为一个整型参数，返回值为布尔型（是否为同构数）。
# #
# def judge_same(n):
#     if n < 10:
#         if (n * n) % 10 == n:
#             return True
#         else:
#             return False
#     else:
#         if (n * n) % 100 == n:
#             return True
#         else:
#             return False
#
#
# if __name__ == '__main__':
#     n = int(input('请输入整数n:'))
#     if judge_same(n):
#         print('YES')
#     else:
#         print('NO')
#

# 简化版
# def judge_same(n):
#     return True if str(n * n)[-len(str(n)):] == str(n) else False
#
#
# if __name__ == '__main__':
#     n = int(input('请输入整数n:'))
#     print('YES') if judge_same(n) else print('NO')

#
# # 1.5
# # 分析下列数据的规律，编写程序完成如下所示的输出。
# # 1
# # 1	1
# # 1	2	1
# # 1	3	3	1
# # 1	4	6	4	1
# # 1	5	10	10	5	1
# # 要求：使用循环结构语句实现。
# list1 = [1]
# for i in range(6):  # 打印六层
#     print(list1)
#     list1.append(1)
#     list2 = list1.copy()
#     for j, s in enumerate(range(len(list1) - 2), start=1):
#         list1[j] = list2[j] + list2[j - 1]
#
# # 1.6
# # 在列表中 20 个不同的整数，找出其中最小的数，将它与第 1 个输入的数交换位置之后输出这些数
# #
# data = input('请依次输入20个数：').split(' ')
# data = list(map(int, data))  # 将列表值转化为整形
# temp = 0  # 替换值
# min_num = data[0]
# for i in data:
#     if i < min_num:
#         min_num = i
# temp = data[data.index(min_num)]
# data[data.index(min_num)] = data[0]
# data[0] = temp
# print(data)
#
# # 简化版
# data = []
# data.extend(int(i) for i in input('请依次输入20个数：').split(' '))
# min_data = min(data)
# data[data.index(min(data))] = data[0]
# data[0] = min_data
# print(data)
# 1.7
# 美国数学家维纳(N.Wiener)智力早熟，11 岁就上了大学。他曾在 1935~1936 年应邀来中国清华大学讲学。
# 一次，他参加某个重要会议，年轻的脸孔引人注目。于是有人询问他的年龄，他回答说：“我年龄的立方是个 4 位数。
# 我年龄的 4 次方是个 6 位数。这 10 个数字正好包含了从 0 到9 这 10 个数字，每个都恰好出现 1 次。”
# 请你编程计算，他当时到底有多年轻。
# 注意：使用循环实现，输出他的年龄在一行。
#
# 第一种方法（转化为字符串拆分）
# for age in range(100):
#     data = []
#     if len(str(age ** 3)) == 4:  # 我年龄的立方是个 4 位数
#         if len(str(age ** 4)) == 6:  # 我年龄的 4 次方是个 6 位数
#             data.extend(str(age ** 3))
#             data.extend(str(age ** 4))
#             # data = [int(i) for i in data] #循环
#             data = list(map(int, data))  # 对象
#             if sum(set(data)) == 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9:
#                 print(age)
# # 第二种方法（数字取余法）
# data = []
# for age in range(100):
#     if len(str(age ** 3)) == 4:  # 我年龄的立方是个 4 位数
#         if len(str(age ** 4)) == 6:  # 我年龄的 4 次方是个 6 位数
#             # 这 10 个数字正好包含了从 0 到9 这 10 个数字
#             data = [age ** 3 % 10, age ** 3 % 100 // 10, age ** 3 % 1000 // 100, age ** 3 // 1000,
#                     age ** 4 % 10, age ** 4 % 100 // 10, age ** 4 % 1000 // 100,
#                     age ** 4 % 10000 // 1000, age ** 4 // 10000 % 10, age ** 4 // 100000]
#             if len(set(data)) == 10:
#                 print(age)

# # 1.8
# # 输入整数 a，输出结果 s，其中 s 与 a 的关系是：s=a+aa+aaa+aaaa+aa...a，最后为 a 个 a。例如 a=2 时，s=2+22=24。
# # 注意：①使用循环结构语句实现。②a 由键盘输入，且 2 ≤ a ≤9。
# #
# a = int(input('输入整数a:'))
# sum_a = 0
# s = 0
# for i in range(a):
#     for j in range(i+1):
#         sum_a += 10 ** j * a
#     s += sum_a
#     sum_a = 0
# print(s)
# 简化版(函数版)
# a = int(input('输入整数a:'))
# s = [str(10 ** i * a) for i in range(a)]  # 存入加数，并转化为字符串
# s = [int(i.replace('0', str(a), i.count('0'))) for i in s]  # 将所有0变化为对应的数字，并重新化为整形
# print(sum(s))

#
# # 1.9
# # 判断一个整数是否是回文数。
# # (1)题目分析：回文数是指正序(从左向右)和倒序(从右向左)读都是一样的整数。
# def split_int(num):  # 差分数字
#     num = str(num)
#     num = ' '.join(num)
#     data = list(map(int, num.split(' ')))
#     # data = []
#     # for i in num:
#     #     data.append(i)
#     # data = list(map(int, data))
#     return data
#
#
# if __name__ == '__main__':
#     data = split_int(input('请输入一个整数：'))
#     for i in range(len(data) // 2):
#         if data[i] != data[len(data) - 1 - i]:
#             print('NO')
#             break
#     else:
#         print('YES')
# 简化版（函数）
# data = ' '.join(input('请输入一个整数：')).split()
# print('YES') if list(reversed(data)) == data else print('NO')
