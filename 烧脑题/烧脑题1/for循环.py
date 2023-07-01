# # 1.1
# # 从键盘接受一个正整数，列出该数字的中文表示格式，例如：键盘输入 123，打印出一二三；键盘输入 3103，打印出三一零三.（考验循环和列表的索引使用）
# #
# data = int(input('请输入一个正整数：'))
# cn_num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
# print_answer = []
# while data:
#     print_answer.append(cn_num[data % 10])
#     data //= 10
# for i in range(len(print_answer) - 1, -1, -1):
#     print(print_answer[i], end='')
# 第二种方法（for循环输出）
# data = []
# data.extend(input('请输入一个正整数：'))
# cn_num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
# for i in data:
#     print(cn_num[int(i)], end='')
# 第三种方法--简化版
# data = [int(i) for i in ' '.join(input('请输入一个正整数：')).split()]
# cn_num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
# for i in data:
#     print(cn_num[i], end='')

# # 1.2
# # 门票的序列号必定是系统里总序列的子序列，请你核对门票的真实性。
# # 从键盘接收两个字符串a 和b，请你判断字符串a 是否包含字符串b，是的话输出“Yes”，否则输出“No”。有多组测试用例，每个测试用例占一行，两个字符串之间用空格隔开。
# # 例如：输入JavaStudy Java 则输出Yes     Student School 则输出 No
# # 注意 ：判断后者是否存在与前者里面  请用循环完成
# #
# a, b = input('按顺序输出字符串a,b:').split(' ')
# for i in range(len(a) - len(b) + 1):
#     if b == a[i:i + len(b)]:
#         print('YES')
#         break
# else:
#     print('NO')

#
# # 1.3 中国结
# # 公司现在需要打印中国结的主结(位于中间，最大的那一个结)，为了打印出漂亮新颖的主结，于是设计打印主结的长度满足可以被 7 整除这个条件。现在公司需要统计某个范围内
# # 能被 7 整除的整数的个数，以及这些能被 7 整除的数的和。
# # 从键盘上输入一个整数 N，输出 1~N 之间能被 7 整除的整数的数，以及这些能被 7 整除的数的和
#
# sum_seven = 0
# data = int(input('请输入一个正整数N：'))
# for i in range(1, data):
#     if i % 7 == 0:
#         sum_seven += i
#         print(i, end=' ')
# print(f'\n被 7 整除的数的和:{sum_seven}')
#
# 简化版
# sum_seven = 0
# data = int(input('请输入一个正整数N：'))
# result = [i for i in range(1, data) if i % 7 == 0]
# print(f'能被 7 整除的整数的数:{result}')
# print(f'被 7 整除的数的和:{sum(result)}')
# # 1.4 项列求和
# # 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13 … 求出这个数列的前 20 项之和。要求：
# # 利用循环计算该数列的和。注意分子分母的变化规律。
# # 注意：
# # a1=2,	b1=1,	c1=a1/b1; a2=a1+b1, b2=a1, c2=a2/b2; a3=a2+b2, b3=a2, c3=a3/b3;
# # …
# # s = c1+c2+…+c20;
# # s 即为分数序列：2/1，3/2，5/3，8/5，13/8，21/13 … 的前 20 项之和。
num_mom = 1  # 分母
num_sun = 2  # 分子
num_sum = 0  # 序列之和
temp = 0  # 替换值
for i in range(20):
    print(i, num_mom, num_sun)
    num_sum += num_sun / num_mom
    temp = num_mom
    num_mom = num_sun
    num_sun = num_sun + temp
print(num_sum)


def sum(data1, data2, t):
    if t == 19:
        return data1 / data2
    else:
        return data1 / data2 + sum(data1 + data2, data1, t + 1)


print(sum(2, 1, 0))
# # 1.5
# # 一个球从 100 米高度自由落下，每次落地后反弹回原高度的一半，再落下，再反弹。
# # 求它在第十次落地时，球共经过多少米? 第十次反弹多高?
# #
# sum_h = 0
# h = 100
# for i in range(10):
#     sum_h += h#相加下落的高度
#     h = h / 2
#     sum_h += h#相加反弹的高度
# print(f'球经过{sum_h-h}米')
# print(f'第十次反弹{h}米高')
#
#
# # #
# # 1.6
# # 求奇数、
# # 编写程序实现：从键盘输入正整数 s，从低位开始取出 s 中的奇数位上的数，依次构成一个新数 t，
# # 高位仍放在高位，低位仍放在低位，最后在屏幕上输出 t。例如，当 s 中的数为 7654321 时，t 中的数为 7531。
# #
# num = int(input('输入一个正整数:'))
# i = 1  # 循环次数判断奇、偶
# remainder = 0  # 余数
# t = 0
# mul = 1  # 乘数
# if num / 10 == 0:
#     t = num % 10
# else:
#     while num:
#         if i % 2 != 0:
#             t += num % 10 * mul
#             mul = mul * 10
#         num = num // 10
#         i += 1
# print(f't的值是{t}')
#
# 简化版(使用枚举)
# num = data = ' '.join(input('请输入一个正整数：')).split()
# for index, data in enumerate(num, start=1):
#     if index % 2 != 0:
#         print(int(data), end='')
#
# # 1.7
# # 在一个停车场内，汽车、摩托车共停了 48 辆，其中每辆汽车有 4 个轮子，每辆摩托车
# # 有 3 个轮子，这些车共有 172 个轮子，编程输出停车场内有汽车和摩托车的数量。
# #
# i = 0  # 汽车数量
# for i in range(1, 49):
#     if i * 4 + (48 - i) * 3==172:
#         print(f"汽车数量是:{i},摩托车数量是：{48-i}")
#
# # 1.8
# # 小明今天参加了“校园歌手大赛”，评委的打分规则是去掉一个最低分和一个最高分后算出剩下分数的平均分，你能帮助小明快速的算出平均分吗？	（评委数量必须大于 2）
# # 输入说明：首先输入一个整数 n，代表评委人数，然后输入 n 个数。请按照题目的计算规则计算出平均分然后输出。
# # 例如输入： 6
# # 100 90 90 80 85 95
# # 按照题目注意计算平均分并输出： 90.0
# #
# n = int(input('输入评委人数:'))
# point = input('输入分数:').split(' ')
# point = list(map(int, point))  # 将列表值转化为整形
# point.remove(max(point))
# point.remove(min(point))
# print(f'平均分为：{sum(point) / len(point)}')
#
# # 1.9九九乘法表
# # 选择乘法口诀助记功能，输出阶梯形式的 9*9 乘法口诀表
# #
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}X{j}={i * j}', end=' ')
#     print()
#
#
# # 1.10
# # 输入一个字符串统计每个字符在字符串中出现的次数。
# #
# char = input('请输入一个字符串:')
# data = []
# count = []
# for i in char:
#     if i in data:
#         count[data.index(i)] += 1
#     else:
#         data.append(i)
#         count.append(1)
# for i in range(len(data)):
#     print(f'{data[i]}:{count[i]}次')
#
# 简化版（利用函数）
# char = input('请输入一个字符串:')
# data = sorted(list(set(char)))  # 去重+排序
# for i in data:
#     print(f'{i}:{char.count(i)}次')
#
# # 1.11
# # 有 n 盏灯，编号 1～n（0<n<100）。第 1 个人把所有灯打开，第 2 个人按下所有编号为
# # 2 的倍数的开关（这些灯将被关掉），第 3 个人按下所有编号为 3 的倍数的开关（其中关掉的灯将被打开，开着的灯将被关闭），
# # 依次类推。输入灯数和人数，输出开着的灯的编号。
# # 比如输入：10 2 输出最后亮灯的编号：1,3,5,7,9 注意：使用循环语句实现。
# #
# n, x = input('请依次输入灯数和人数:').split(' ')
# n = int(n)
# x = int(x)
# led = []
# # 使输入的所有灯打开
# for i in range(n + 1):
#     led.append(1)
# for i in range(2, x + 1):
#     for j in range(i, n + 1, i):
#         led[j] = -led[j]
# for i in range(1, n + 1):
#     if led[i] == 1:
#         print(i, end=',')
# 简化版
# n, x = input('请依次输入灯数和人数:').split(' ')
# n, x = int(n), int(x)
# led = [1 for i in range(n + 1)]
# for i in range(2, x + 1):
#     for j in range(i, n + 1, i):
#         led[j] = -led[j]
# for i in range(1, n + 1):
#     if led[i] == 1:
#         print(i, end=',')

# # 冒泡排序、
# # 原始数组：[1,9,3,7,4,2,5,0,6,8]
# # 排序后：[0,1,2,3,4,5,6,7,8,9]；
# # 要求：综合使用分支、循环结构语句实现，直接输出结果不计分。打印每一次运行的结果
# #
# initial = [1, 9, 3, 7, 4, 2, 5, 0, 6, 8]  # 初始值
# temp = 0  # 中间值转化
# for i in range(len(initial)):
#     for j in range(len(initial) - i-1):
#         if initial[j] > initial[j + 1]:
#             temp = initial[j]
#             initial[j] = initial[j + 1]
#             initial[j + 1] = temp
#     print(f'第{i+1}轮变化结果：{initial}')
#
# # 1.13
# # 动物园饲养的食肉动物分大型动物和小型动物两类，规定老虎、狮子一类的大动物每次喂肉每头三斤，
# # 狐狸、山猫一类小动物每三头喂一斤。该动物园共有这两类动物 100 头，每
# # 次需喂肉 100 斤，编程输出大、小动物的数量。
# #
# for big in range(1, 101):
#     if 3 * big + 1 / 3 * (100 - big) == 100:
#         print(f'大型动物{big}，小型动物{100 - big}')
#
# # 1.14
# # 从键盘接收一个整数 n(n>=4)，请打印一个由“*”号组成的长度和宽度均为 n 的空心矩形。例如输入：4 你要在屏幕打印如下图形：
# # ****
# # *  *
# # *  *
# # ****
# n = int(input('请输入一个整数n：'))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             print('*', end='')
#         else:
#             print('', end=' ')
#     print()
#
# #
# # 1.15
# # 注意输出指定空心正方形。输入第一个数字为边长，第二个字符为组成图形边的字符。例如：输入
# # 4 a  （4为空心正方形的大小，a为显示的字符）
# # 输出
# # aaaa
# # a  a
# # a  a
# # aaaa
# n, char = input('请依次输入边长和字符：').split(' ')
# n = int(n)
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             print(f'{char}', end='')
#         else:
#             print('', end=' ')
#     print()
#
#
# # 1.16
# # 已知鸡和兔的总数量为 n,总腿数为 m。输入 n 和 m,依次输出鸡和兔的数目，如果无解， 则输出“No  answer”(不要引号)
# n, m = input('依次输入n,m:').split(' ')
# n = int(n)
# m = int(m)
# rabbit = 0
# f = True  # 判断答案是否存在
# for rabbit in range(n + 1):
#     if rabbit * 4 + (n - rabbit) * 2 == m:
#         f = False
#         print(f'兔的数量：{rabbit}，鸡的数量：{n - rabbit}')
# if f:
#     print('No answer')
#
# # 1.17
# # 中国古代的《算经》记载了这样一个问题：公鸡 5 文钱 1 只，母鸡 3 文钱 1 只，小鸡 1
# # 文钱 3 只，如果用 100 文钱买 100 只鸡，那么公鸡、母鸡和小鸡各应该买多少只呢？现在请
# # 你编程求出所有的解，每个解输出 3 个整数，打印在一行，用空格隔开，分别代表买的公鸡、母鸡、小鸡的数量。
# # 注意：100 文钱要正好用完。请输出所有的解，每个解占一行。
# #
# #
# cock, hen, chick = 0, 0, 0  # 公鸡，母鸡，小鸡
# for cock in range(100):
#     for hen in range(100):
#         for chick in range(100):
#             if cock + hen + chick == 100 and cock * 3 + hen * 1 + 1 / 3 * chick == 100:
#                 print(cock, hen, chick, sep=' ')
#
#
# # 1.18
# # 啤酒每罐 2.3 元，饮料每罐 1.9 元。小明买了若干啤酒和饮料，一共花了 82.3 元。
# # 我们还知道他买的啤酒比饮料的数量少，请你编程计算他买了几罐啤酒。
# #
# max_beer = int(82.3 / 2.3)
# max_drink = int(82.3 / 1.9)
# for beer in range(max_beer):
#     for drink in range(max_drink):
#         if beer * 2.3 + drink * 1.9 == 82.3 and beer < drink:
#             print(beer)
#
# # 1.19 折纸比高、
# # 假设一张足够大的纸，纸张的厚度为 0.5 毫米。请问对折多少次以后，可以达到珠穆朗玛峰的高度(最新数据：8844.43 米)。
# # 请编写程序输出对折 次数。
# # 注意：使用循环结构语句实现，直接输出结果不计分。
# #
# sum_height = 0.5
# t = 0  # 折纸次数
# while sum_height < 8844430:
#     sum_height *= 2
#     t += 1
# print(t)

# # 1.20
# # 职员小 A 今天犯了一个致命的错误，他一不小心丢失了 X 项目的市场调查结果只记得一个
# # 公式 xyz+yzz=532，其中 x、y、z 均为一位数，现在请你帮忙编写一个程序求出 x、y、z 分别代表什么数。
# #
# #
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             if (x * 100 + y * 10 + z) + (y * 100 + z * 10 + z) == 532:
#                 print(x, y, z)

# # 1.21
# # 小明带两个妹妹参加元宵灯会。别人问她们多大了，她们调皮地说：“我们俩的年龄之积是年龄之和的 6 倍”。
# # 小明又补充说：“她们可不是双胞胎，年龄差肯定也不超过 8 岁啊。” 请你编程求出小明的较小的妹妹的年龄。
# #
# age_min = 0
# age_max = 0
# for age_min in range(1, 50):
#     for age_max in range(1, 50):
#         if age_min * age_max == (age_max + age_min) * 6 and 0 < age_max - age_min <= 8:
#             print(age_min)

# # 1.22
# # 本月酒水的销售为 2!+4!+5!的值。n!表示 n 的阶乘，例如 3!=3×2×1=6，5!=5×4×3
# # ×2×1=120。求这个值
# #
# sum_num = 0
# t = 1  # 计算每次循环的值
# for i in range(1, 6):
#     t *= i
#     if i == 2:
#         sum_num += t
#     if i == 4:
#         sum_num += t
#     if i == 5:
#         sum_num += t
# print(sum_num)
# 第二种方法（函数）
# def value_factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num
#
#
# print(value_factorial(2) + value_factorial(4) + value_factorial(5))
#
# # 1.23
# # 分别输入两个字符串 s1 和 s2 ，请问 s1 中包含多少个 s2，如果没有则输出 0。要求：使用循环。
# #
# #
# s1, s2 = input('按顺序输出字符串s1,s2:').split(' ')
# t = 0  # 计数器
# for i in range(len(s1) + 1):
#     if s2 == s1[i:i + len(s2)]:
#         t += 1
# print(t)
#
# # 1.24
# # 小米打算把图标设计成下面这样，但是他不知道几层最合适，于是想写个程序，打印出不同层的图标，请你帮帮他。
# # —
# # ———
# # —————
# # ———————
# # 注意：输入 n，打印 n 层高度的图标，如图是 4 层。
# #
# n = int(input('请输入n:'))
# for i in range(n):
#     for j in range(n - i):
#         print(' ', end='')
#     for j in range(1 + 2 * i):
#         print('-', end='')
#     print()

# # 1.26
# # Lee 的老家住在工业区，日耗电量非常大。
# # 今年 7 月，传来了不幸的消息，政府要在 7、8 月对该区进行拉闸限电。政府决定从 7
# # 月 1 日起停电，然后隔一天到 7 月 3 日再停电，再隔两天到 7 月 6 日停电，依次下去，每次都比上一次长一天。
# # Lee 想知道自己到家后到底要经历多少天倒霉的停电。请编写程序帮他算一算。
# # 注意：从键盘输入放假日期、开学日期，日期限定在 7、8 月份，且开学日期大于放假日期，然后在屏幕上输出停电天数。
# # 提示：可以用数组标记停电的日期。
# date7 = [f'7-{i}' for i in range(1, 32)]
# date8 = [f'8-{i}' for i in range(1, 32)]
# date_time = date7 + date8
#
# date_dict = {}
# start = 0
# s = 1
# for index, i in enumerate(date_time):
#     date_dict[i] = 0
#     if start == index:
#         date_dict[i] = 1
#         s += 1
#         start = start + s
#
# print(date_dict)
# date_list = list(date_dict.keys())
#
# start_date = input('请输入开始的时间')
# stop_date = input('请输入截至的时间')
#
# start_index = date_list.index(start_date)
# stop_index = date_list.index(stop_date)
#
# power_cut = []
# for i in range(start_index, stop_index + 1):
#     if date_dict[date_list[i]] == 1:
#         power_cut.append(date_list[i])
#
# print(power_cut)
# print(len(power_cut))
#
#
# # 1.27
# # 物园里新来了两只骆驼，那么你能计算出它们年龄的最小公倍数么？ 从键盘输入两个整数，输出两个整数的最小公倍数。
# #
# #
# age_a, age_b = input('依次输入两个整数：').split(' ')
# age_a = int(age_a)
# age_b = int(age_b)
# temp = 0  # 替换值
# if age_b > age_a:
#     temp = age_b
#     age_b = age_a
#     age_a = temp
# i = age_a  # 计数器
# while 1:
#     if i % age_a == 0 and i % age_b == 0:
#         print(i)
#         break
#     i *= 2
#
# # 1.28
# # 问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
# # 假设向程序提供以下输入:8
# # 则输出为:
# # {1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}
# # 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。考虑使用dict类型()
# #
# n = int(input('请输入整数n:'))
# dict_1 = {}
# for i in range(1, n + 1):
#     dict_1[i] = i ** 2
# print(dict_1)
#


# # 1.29
# # 编写一个接受句子的程序，并计算大写字母和小写字母的数量。
# # 假设为程序提供了以下输入：
# # Hello world!
# # 然后，输出应该是：
# # 大写实例 1
# # 小写实例 9
# char = input('请输入字符串:')
# small = 0
# big = 0
# for i in char:
#     if i.isupper():
#         big += 1
#     elif i.():
#         small += 1
# print(f'大写实例 {big}')
# print(f'小写实例 {small}')
# 简化版
# char = input('请输入字符串:')
# small = [i for i in char if i.islower()]
# big = [i for i in char if i.isupper()]
# print(f'大写实例 {len(big)}')
# print(f'小写实例 {len(small)}')
