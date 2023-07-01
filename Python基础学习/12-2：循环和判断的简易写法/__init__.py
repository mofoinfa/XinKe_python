# 家庭作业
# 1到100内(不包括1和100)的所有奇数和
sum_num = 0
for i in range(2, 100):
    if i % 2 != 0:
        sum_num += i
print(sum_num)
# 简化模式
print(sum(i for i in range(2, 100) if i % 2 != 0))

# 所学内容
# 一、列表推导式
# # 普通写法
# list_data = []
# for i in range(10):
#     if i % 2 == 0:
#         list_data.append(i)
#
# print(list_data)
# 推导写法
# list_data = [i for i in range(10) if i % 2 == 0]
# print(list_data)

# 二、三元表达式
# 例题1、
# 普通写法
# age = 20
# if age > 18:
#     print('成年')
# else:
#     print('非成年')

# print('成年') if age > 18 else print('非成年')# 推导写法

# 例题2、
# age = 20
# if age > 18:
#     data = 1
# else:
#     data = 0
# print(data)
#
# data = 1 if age > 18 else 0
# print(data)


# 二、混合写法
# 1.加if和else
# list_data = [i if i % 2 == 0 else str(i) for i in range(10)]
# print(list_data)
# 2.只有if
# 例题：求1 - 10内的奇数数列
# data = [i for i in range(10) if i % 2 != 0]
# print(data)
