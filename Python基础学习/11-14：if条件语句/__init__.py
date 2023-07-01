# 家庭作业
# 通过input函数输入一个学生的成绩
# 判断他的学习成绩，
#
# 大于等于90为优秀，输出优秀
#
# 60到89分为及格，输出及格
#
# 低于60分为不及格，输出不及格

point = input('请输入学生的成绩:')
try:  # 如果用户输入的为字符串类型则抛出异常，并提示分数应该是整型或小数的变量
    point = float(point)  # 转化为小数比较
    if point >= 90:  # 大于90的情况
        print('优秀')
    elif 60 <= point < 90:  # 60到90之间的情况
        print('及格')
    else:  # 有可能输入的是一个负数
        if point < 0:  # 当输入为负数时提示输入格式错误
            print('分数格式输入错误')
        else:  # 输出最后一种情况呢
            print('不及格')
except:  # 抛出异常提示
    print('请输入整数或小数')

# 所学内容
# 1）if if 和 if elif的区别
#   if，if为并行，一个结束后为继续执行另外一个
#   if，elif为串行执行一个正确的判断后终止运行


# 例题
# 18岁的打工情况
# try:
#     age = int(age)
#     if age < 18:
#         print('你是童工')
#     elif age > 60:
#         print('你退休了')
#     else:
#         print('你是合法工作年龄')
# except:
#     print('请输入整数')
# a = "打雷"
# if a == '打雷':
#     print(123)
# elif a == '打雷':
#     print(1234)
# # 做公交车
# money = input('请输入你当前的money:')
# seat = 0
# try:
#     money = int(money)
#     if money > 0:
#         print("小王上车了")
#         if seat == 0:
#             print("小王有座位了")
#         else:
#             print("小王站着")
#     else:
#         print('小王没成功上车')
# except:
#     print('请输入整数')
# if 0.00:
#     print(123)
# else:
#     print(12)
