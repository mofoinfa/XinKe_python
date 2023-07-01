# # 1.1
# # 一个猪圈里有2只刚满2岁的猪，
# # 每只猪只能活4年，每只猪第四年还可以生一次崽
# # 2岁后每2只猪每年可以生4头小猪（假设小猪性别比例总是1：1），
# # 问n年后猪圈里有几只猪？
# # 解题思路：
# # 因为小猪性别比例总是1：1，所以两只小猪比作1只，最后总数*2
# # 草稿
# # 第一年:2,2
# # 第二年:3,3,1,1,1,1
# # 第三年:2,2,2,2,1,1,1,1
# # 第四年:3,3,3,3,2,2,2,2,1,1,1,1,1,1,1,1
# pig_num = [2]
# n = int(input('请输入n年：'))
# for i in range(n):  # 每一年进行增改
#     for j in range(len(pig_num)):
#         pig_num[j] += 1  # 每一年增加一岁
#         if pig_num[j] > 2:  # 2岁后每2只猪每年可以生4头小猪(因为小猪性别比例总是1：1，所以两只小猪比作1只)
#             pig_num += [1, 1]
#         if pig_num[j] == 4:  # 四年后猪死了
#             del pig_num[j]
# print(f'第{n+1}年：{len(pig_num) * 2}只猪')

# # 1.2
# # 题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
# # 提示：考虑使用yield。
# #
# def foo(n):
#     i = 0
#     while i < n:
#         j = i
#         i = i + 1
#         if j % 7 == 0:
#             yield j
#
#
# if __name__ == '__main__':
#     n = int(input('请输入正整数n:'))
#     for i in foo(n):
#         print(i)
#
#
# # 1.3
# # 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# #
# # 上面是由数组[0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# # 解题思路：层层判断，判断一层后所有层数减1
# #
# n = input('请依次输入柱子高度非负整数n:').split(' ')
# n = list(map(int, n))  # 转化为整数
#
#
# # n = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# # 判断该雨滴是否能被接收
#
# def judge_is_rain(transverse, data):  # 该点的横坐标，纵坐标，值
#     left = False
#     right = False
#     #
#     for i in range(len(n)):
#         if n[i] > data and i < transverse:  # 判断左边是否有大于该点的值
#             left = True
#         if n[i] > data and i > transverse:  # 判断右边是否有大于该点的值
#             right = True
#     if left and right and data == 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     t = 0  # 计数器
#     sum_rain = 0  # 雨滴总数
#     while t != len(n):
#         t = 0
#         for i in range(len(n)):
#             if judge_is_rain(i, n[i]):  # 获取雨滴
#                 sum_rain += 1  # 总雨滴数+1
#                 n[i] += 1  # 补充该与滴的位置
#             else:
#                 t += 1  # 不满足的层数+1
#         else:  # 每判断一层后层数减1
#             for i in range(len(n)):
#                 n[i] = n[i] - 1
# print(sum_rain)


# 1.3 改进版
#
# 接雨水从2D变成3D  长宽12 简单示例：
#
# 在这种情况下，可以接 多少个单位的雨水呢？
# pillar = [[0, 1, 5, 2, 6, 5, 4, 3, 2, 2, 2],
#           [1, 3, 3, 2, 1, 0, 1, 4, 1, 1, 1],
#           [3, 4, 0, 2, 1, 0, 1, 1, 2, 4, 2],
#           [0, 1, 3, 2, 1, 0, 1, 3, 1, 1, 0],
#           [3, 2, 1, 2, 1, 1, 5, 3, 6, 4, 2],
#           [0, 1, 6, 2, 1, 0, 0, 1, 2, 1, 0],
#           [0, 1, 3, 2, 1, 2, 1, 2, 3, 4, 2],
#           [1, 1, 6, 2, 2, 0, 4, 3, 2, 1, 0],
#           [0, 1, 4, 2, 1, 2, 1, 2, 4, 4, 2],
#           [1, 2, 3, 2, 3, 0, 3, 2, 2, 1, 1], ]  # 所有的柱子数量
# m = 10  # 长
# n = 11  # 宽
#
#
#
#
#
# # 判断这个雨滴是否在可以收集
# def judge_is_rain(transverse, longitudinal, data):  # 该点的横坐标，纵坐标，值
#     left, right, before, behind = False, False, False, False
#     # 判断左边是否有峰值
#     for i in range(longitudinal - 1, -1, -1):
#         if pillar[transverse][i] > 0:
#             left = True
#     # 判断右边是否有峰值
#     for i in range(longitudinal + 1, n):
#         if pillar[transverse][i] > 0:
#             right = True
#     # 判断上方是否有峰值
#     for j in range(transverse - 1, -1, -1):
#         if pillar[j][longitudinal] > 0:
#             before = True
#     # 判断下方是否有峰值
#     for j in range(transverse + 1, m):
#         if pillar[j][longitudinal] > 0:
#             behind = True
#     if left and right and before and behind and data == 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     sum_rain = 0  # 总水滴量
#     t = 0  # 计数器
#     ii = 0
#     # print(len(pillar))
#     # print(pillar[0][3])
#     while t != n * m:
#         ii += 1
#         t = 0
#         for i in range(m):
#             for j in range(n):
#                 # print(f'piller[{i}][{j}]={pillar[i][j]}')
#                 if judge_is_rain(i, j, pillar[i][j]):
#                     # print(i, j, pillar[i][j], ii)
#                     pillar[i][j] += 1
#                     sum_rain += 1  # 总水滴量
#                 elif pillar[i][j] < 0:
#                     t += 1
#         else:
#             # 所有层数减小1
#             for i in range(m):
#                 for j in range(n):
#                     pillar[i][j] -= 1
#     print(sum_rain)
