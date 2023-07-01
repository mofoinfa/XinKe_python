# # 1.1
# # 编写程序计算购买图书的总金额：用户输入图书的定价和购买图书的数量，
# # 并分别保存到一个 float 和一个 int 类型的变量中，然后根据用户输入的定价和购买图书的数量，
# # 计算购书的总金额并输出。其中，图书销售策略为：正常情况下按 9 折出售，购书数量超过 10本打
# # 8.5 折，超过 100 本打 8 折
# num = int(input('请输入购买书的数量:'))  # 书的数量
# price = float(input('请输入购买书的价格:'))  # 书的价格
# if 10 < num <= 100:
#     print((num * price) * 0.85)
# elif num > 100:
#     print((num * price) * 0.8)
# else:
#     print((num * price) * 0.9)
#
#
# # 1.2
# # 动物园想在新建一个三角形的人工湖，一是为了养鱼美观，二是可以循环水资源。从键盘输入三条边 A、B、C 的边长，
# # 请编程判断能否组成一个三角形。（可以组成三角形的要素，两边之和大于第三边，两边之差小于第三边）
# # 要求：如果三条边长 A、B、C 能组成三角形的话，输出 YES，否则 NO。
# a = float(input('请输入A边:'))
# b = float(input('请输入B边:'))
# c = float(input('请输入C边:'))
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')
#
# # 简化版
# a, b, c = input('请依次输入A,B,C边:').split()
# a, b, c = float(a), float(b), float(c)
# print('YES') if a + b > c and a + c > b and b + c > a else print('NO')

# # 1.3
# # 商店A 准备在今年夏天开始出售西瓜，西瓜的售价如下，20 斤以上的每斤 0.85 元；
# # 重于 15 斤轻于等于 20 斤的，每斤 0.90 元；重于 10 斤轻于等于	15 斤的，
# # 每斤 0.95 元；重于 5 斤轻于等于 10 斤的，每斤 1.00 元；轻于或等于 5 斤的，
# # 每斤 1.05 元。现在为了知道商店是否会盈利要求 A 公司帮忙设计一个输入西瓜的重量和顾客所付钱数，
# # 输出应付货款和应找钱数的程序。
# weight = float(input('请输入西瓜的重量:'))
# price = float(input('顾客所付钱数：'))
# repay = 0
# money = 0
# if weight > 20:
#     money = weight * 0.85
# elif 15 < weight <= 20:
#     money = weight * 0.9
# elif 10 < weight <= 15:
#     money = weight * 0.95
# elif 5 < weight <= 10:
#     money = weight * 1
# else:
#     money = weight * 1.5
# repay = price - money
# if repay < 0:
#     print(f'商品的价格是{money}元')
#     print(f'你所支付的钱不够，你还需支付{-repay}元')
# elif repay == 0:
#     print('你所支付的钱刚刚好')
# else:
#     print(f'商品的价格是{money}元')
#     print(f'找零{repay}元')
#
#
#
# # 1.4
# # 对学生成绩进行统计和数据分析可以发现学生对知识的掌握情况，以便教师根据分析的结果调整教学内容和重难点，
# # 现在需要完成以下任务来实现成绩分析系统。
# # 输入一个百分制的成绩 t，将其转换成对应的等级然后输出，具体转换规则如下：
# # 90~100 为 A
# # 80~89 为 B
# # 70~79 为 C
# # 60~69 为 D
# # 0~59 为 E
# # 要求：如果输入数据不在 0~100 范围内，请输出一行错误提示：“数据超出范围！”
# grade = float(input('请输入成绩:'))
# if 90 <= grade < 100:
#     print('A')
# elif 80 <= grade < 90:
#     print('B')
# elif 70 <= grade < 80:
#     print('C')
# elif 60 <= grade < 70:
#     print('D')
# else:
#     print('E')
#
# # 1.5
# # 从键盘接收一个十一位的数字，判断其是否为尾号 5 连（最后5个数一样）的手机号。规则：第 1 位是 1，
# # 第二位可以是数字 358 其中之一，后面 4 位任意数字，最后 5   位为任意相同的数字。例如：
# # 18601088888、13912366666 则满足。
# # 注意：不满足的输出“false”，满足要求的输出“true”。
# #
# #
# phone = int(input('请输入手机号码:'))
# one = phone // 10000000000  # 第一位
# two = phone // 1000000000 % 10  # 第二位
# last_five = [phone % 10, phone % 100 // 10, phone % 1000 // 100, phone % 10000 // 1000,
#              phone % 100000 // 10000]  # 最后五位
# if one == 1:  # 第 1 位是 1
#     if two == 3 or two == 5 or two == 8:  # 第二位可以是数字 358 其中之一
#         if len(set(last_five)) == 1:  # 最后5位为任意相同的数字(集合去重只剩下一个)
#             print("true")
#         else:
#             print("false")
#     else:
#         print("false")
# else:
#     print("false")
#
# 第二种方法（精简版）
# phone = (input('请输入手机号码:'))
# phone = list(map(int, (' '.join(phone)).split()))
# print("true") if phone[0] == 1 and phone[1] == 3 or phone[1] == 5 or phone[1] == 8 and len(
#     set(phone[-5:])) == 1 else print("false")

# # 1.6
# # 按顺序输入正方形的边长（a），长方形的长（l）和宽（d），以及圆的半径（r），计算并比较它们哪个图形面积更大，输出面积最大的图形。
# # 例如：输入 1 3 4 1，输出：长方形
# #
# a, l, d, r = (input('按顺序输入正方形的边长（a），长方形的长（l）和宽（d），以及圆的半径（r）:')).split(' ')
# a = float(a)
# l = float(l)
# d = float(d)
# r = float(r)
# area = [a * a, l * d, r ** 2 * 3.14]
# graphics = ['正方形', '长方形', '圆形']
# print(graphics[area.index(max(area))])
#
# # 1.7
# # 整除判断游戏能显著提高小朋友的逻辑思维能力，问题要求如下：
# # •能同时被 3、5、7 整除
# # •能同时被 3、5 整除
# # •能同时被 3、7 整除
# # •能同时被 5、7 整除
# # •只能被 3、5、7 中的一个整除
# # •不能被 3、5、7 任一个整除
# # 输入一个整数，输出满足对应条件的结果。要求：使用分支结构语句实现。
# #
# data = int(input('请输入一个整数：'))
# if data % 3 == 0 and data % 5 == 0 and data % 7 == 0:
#     print('能同时被 3、5、7 整除')
# elif data % 3 == 0 and data % 5 == 0:
#     print('能同时被 3、5 整除')
# elif data % 3 == 0 and data % 7 == 0:
#     print('能同时被 3、7 整除')
# elif data % 5 == 0 and data % 7 == 0:
#     print('能同时被 5、7 整除')
# elif data % 5 == 0 or data % 7 == 0 or data % 3 == 0:
#     print('只能被 3、5、7 中的一个整除')
# else:
#     print('不能被 3、5、7 任一个整除')
#
# 1.8
# # 判断一个整数是否为“水仙花数”。所谓“水仙花数”是指一个三位的整数，其每个单独数字的立方和等于该数本身。例如：153 是一个“水仙花数”， 例如 153=1**3＋5**3＋3**3。
# # 如果是水仙花数就输出YES,否则就输出No
# data = int(input('请输入一个三位的整数：'))
# if data == (data // 100) ** 3 + (data // 10 % 10) ** 3 + (data % 10) ** 3:
#     print('YES')
# else:
#     print('NO')
# 简化版
# data = int(input('请输入一个三位的整数：'))
# print('YES') if data == (data // 100) ** 3 + (data // 10 % 10) ** 3 + (data % 10) ** 3 else print('NO')
