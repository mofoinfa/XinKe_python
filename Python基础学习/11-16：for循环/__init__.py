# 家庭作业
# 题目：找数字找出0-100之间的数据找出偶数 并且可以被4和5整除(不包含0和100)的整数
a = []  # 创建数组
b = []  # 创建数组
c = []  # 能被4和5同时整除
for i in range(2, 100, 2):  # 确保使用的数据为0-100之间的偶数
    if i % 4 == 0:  # 可以被四整除
        a.append(i)
    if i % 5 == 0:
        b.append(i)  # 可以被五整除
    if i % 5 == 0 and i % 4 == 0:
        c.append(i)
# 输出结果
print(f'被四整除的整数:{a}')
print(f'被五整除的整数:{b}')
print(f'能同时被四和五整除的整数:{c}')
# 所学内容
# range
# 使用方法：1)一种参数：range(结束值)#此时的开始值默认为0,步长默认为1
#         2）两种参数：range(开始值，结束值)#步长默认为1
#         3）三种参数：range（开始值，结束值，步长）
# 注意：结束的实际值比所写的数字小1
#
# #else在for中的运用
# for a in range(3):
#     if a==1:
#         print("无意义")
#         pass
#     if a==2:
#         print("结束此次循环")
#         continue
#     if a==3:
#         print("跳出此次循环")
#         break
# else:# 在正常结束循环的时候会运行  查找数据
#    print('正常结束后执行')
# 注意:提前终止循环(break)后不会执行此else的命令

# 循环的概念
# a = 'abc'
# i = 0
# for i in a:
#     print(123)
# print(i)
# # else:
# #     print('112')
# # print(i)

# 输出空心4*4正方形
# for i in range(4):
#     for j in range(4):
#         if i == 1 and j == 1 or i == 1 and j == 2 or i == 2 and j == 1 or i == 2 and j == 2:
#             print(' ', end='')
#             continue
#         print('*', end='')
#     print()
# print()
