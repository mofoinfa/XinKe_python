# 家庭作业
# 需要使用while循环
# 获取1-300（包含1,300）的奇数进行累加, 但是逢7的倍数跳过, 不加进来
i = 1  # 计数器
sum_num = 0  # 所有奇数的累加之和，7排除
while i < 300:
    if i % 2 != 0:  # 所有奇数之和
        if i % 7 == 0:  # 被7整除的排除
            pass
        else:
            sum_num += i  # 所有数字进行累加
    i += 1  # 每次i进行+1操作
print(sum_num)
# 所学内容
# break 语句	在语句块执行过程中终止循环，并且跳出整个循环
# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。

# i = 1
# while i < 10:
#     if i == 5:
#         print(f'第{5}苹果吃饱了，不吃了')
#         break
#     print(f'我正在吃第{i}个苹果')
#     i += 1


# i = 1
# while i < 10:
#     if i == 5:
#         print(f'第{5}苹果吃出虫子,这个苹果不吃了')
#         i += 1
#         continue
#     print(f'我正在吃第{i}个苹果')
#     i += 1
