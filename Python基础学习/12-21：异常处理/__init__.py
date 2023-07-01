# 家庭作业
# 1）定义is_password函数，判断密码是否符合长度
#
# 2）使用input输入密码，使用函数来判断密码长度
#
# 3）如果用户输入长度<8，抛出异常(可以使用自定义异常)
#
# 4）如果用户输入长度>=8，返回(return)输入的密码
# class LengthError(Exception):
#     pass
#
#
# # raise LengthError('123')
# def is_password(password):
#     if len(password) < 8:
#         raise LengthError('密码长度不对 error')
#     else:
#         return password
#
#
# print(is_password(input('请输入密码（密码大于8位）：')))

# 所学内容
# 一、捕获异常
# 1.定义：当遇到异常 程序直接结束
# 2.格式：
# try:
#     可能发⽣错误的代码
# except ValueError:
#     抛出错误类型的异常
# except Exception as e:
#     抛出其他异常
#     print(f'其他的异常：{e}')#e是错误的简单描述

# 二、自定义异常
# 1.定义：代码给别人用 当别人输出错误参数  合作开发  报出错误提示使用者
# 2.例题：一个数字<8为异常，不断输入，直到输入正确停止

# class dataError(Exception):
#     pass
#
#
# while True:
#     data = int(input('请输入一个数字:'))
#     try:
#         if data < 8:
#             raise dataError('输入数字异常')  # 调用自定义异常
#         print('正确')
#         break
#     except dataError:  # 抛出自定义异常
#         print('输入数字异常')
