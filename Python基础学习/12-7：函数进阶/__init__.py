# 家庭作业
# 定义一个模拟ATM机操作的场景
# 1）需要一个存钱和取钱的函数
# 2）设置全局默认资金1000
# 3）调用存钱函数，存放800元，并将操作后函数将余额打印出来(1000+800=1800)
# 4）调用取钱函数，取钱500元，并将操作后函数将余额打印出来(1800-500=1300)
money = 1000


def save_money(change_money):
    global money
    money += change_money


def take_money(change_money):
    global money
    money -= change_money


save_money(800)
print(f'存入800后总资金为：{money}')
take_money(500)
print(f'拿走500后总资金为：{money}')

# 所学内容
# 一、全局变量
# 定义：可变数据类型可以在函数里可以被更改，不可变数据类型需要定义global
# 可变数据类型：列表，集合，字典
# 例题如下
# list_data = [1, 2]
# int_data = 1
#
#
# def change_data():
#     list_data.append(3)
#     global int_data
#     int_data = 2


# 二、*arg,**arg的使用（不定义参数）
# 定义：可以接收无穷多的参数
# def input_data(*args):
#     print(args)
# input_data('蛋挞','面包','可乐')


# 三、可变数据类型赋值的区别
# a+=1#表示在当前地址改变地址的值
# a=a+1#表示重新创建一个数组，并且值等于a+1
