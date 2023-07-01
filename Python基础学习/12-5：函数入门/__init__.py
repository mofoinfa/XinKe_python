# 家庭作业
# 1)定义一个去除重复数据函数,
# 2)传入一个列表参数[3,4,2,2,4,0,1,4],
# 3)请将列表数据去重后进行返回(return)
# 4)在外部输出去重的列表

# 第一种方法：创建一个新数组
def remove_repeat(list_data):
    list_result = []
    for i in list_data:
        if i not in list_result:
            list_result.append(i)
    return list_result


print(f'第一种结果：{remove_repeat([3, 4, 2, 2, 4, 0, 1, 4])}')


# 第二种方法：更改当前数组
def remove_repeat(list_data):
    for i in list_data:
        if list_data.count(i) > 1:
            list_data.remove(i)
    return list_data


print(f'第二种结果：{remove_repeat([3, 4, 2, 2, 4, 0, 1, 4])}')

# 所学内容
# 一、函数的定义
# def add():
#     pass
# 注意：使用函数都需要加一个括号有自己的功能，不加括号代表整个函数，加括号是使用函数
#
# 二、函数的作用
# 1.
# 减少内存空间，方便代码的管理和维护
# 2.
# 对代码进行封装，让代码可以重复使用
#
# 三、函数的使用
# add(data1, data2)  # 调用有参函数
# add()  # 调用无参函数
#
# 四、参数的传入和传出
# # 封装代码
# 例题：传入两个列表，将两个列表合并后求和/平均值输出，用函数实现
# def add(list1, list2):
#     l = list1 + list2
#     return sum(l), sum(l) / len(l
# sum_num, avg_num = add([1, 2], [1, 3])
#
# 五、注释使用(详细)
# def annotation():
#     #快捷键（输入6个双引号按回车）
#     """ # 更加详细说明文档
#    获取容器中的数据个数
#    :param list_data: 可迭代对象
#    :return: 数字
#    """


