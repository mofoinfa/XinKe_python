# 1 输入三条边，判断是否可以组成三角形，根据三边，判断三角形是否是直角三角形，等腰三角形，等边三角形，
# 普通的三角形，输出对于的三角形类型
# 判断是否为直角
def judge_right(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


# 判断是否为等腰
def judge_same(a, b):
    if a == b:
        return True
    else:
        return False


if __name__ == '__main__':

    a, b, c = input('请依次输入三角形的三条边：').split()
    a, b, c = float(a), float(b), float(c)
    if a + b > c and a + c > b and b + c > a:  # 判断是否为三角形
        print('此三角形为：', end='')
        # 判断三角形的种类
        if a == b == c:
            print('等边', end='')
        elif judge_same(a, b) or judge_same(a, c) or judge_same(b, c):  # 判断是否为等腰
            print('等腰', end='')
        if judge_right(a, b, c) or judge_right(b, c, a) or judge_right(a, c, b):  # 判断是否为直角
            print('直角', end='')
        print('三角形')
    else:
        print('此三边不能构成三角形')

# 2完美数
# 第二个问题是找出1000以内的完全数。所谓的完全数，就是除了自身之外，
# 它所有的因子之和等于这个数本身。例如6，它的所有因子是1、2、3，1+2+3=6，
# 故6是完美数。那么在1000以内，完美数一共有6，28，496这三个。
#
factor = []
for i in range(1, 1000):
    for j in range(1, i // 2 + 1):  # 判断是否是因子
        if i % j == 0:
            factor.append(j)
    if sum(factor) == i:
        print(i, end=' ')
    factor = []  # 每轮结束重置因子

# 3斐波那契问题
# 斐波那契数列(Fibonacci sequence)，又叫黄金分割数列。
# 例如1、1、2、3、5、8、13、21、34、55、89......指的是从第三数开始往后，
# 这个数等于前两个数的和，依次往下进行。该问题是求100以内的斐波那契数列。
#
t = 1  # 计数器
list_fibonacci = [1, 1]
while list_fibonacci[t] < 100:
    list_fibonacci.append(list_fibonacci[t] + list_fibonacci[t - 1])
    t += 1
list_fibonacci.pop()  # 删除最后一个大于100的
print(list_fibonacci)

# 4，现有2元、3元、5元共三种面额的货币，如果需要找零99元，一共有多少种找零的方式？
#
t = 0  # 计数器
for two in range(99 // 2):
    for three in range(99 // 3):
        for five in range(99 // 5):
            if 2 * two + 3 * three + 5 * five == 99:
                # print(two,three,five)
                t += 1
print(t)

# 5 有一个随机的二维数组，要求根据列进行排序 输出排序后的矩阵
#
# eg:由于题目没说清，我这里默认随机二维数组的行、列可能范围在（1~10）之间，二维数组里面的值范围在（0~100）
# 按照从小到大和从大到小的两种顺序进排序
# 第一种情况从小到大
import random

line = random.randint(1, 10)  # 行
column = random.randint(1, 10)  # 列
list_data = []
temp = 0  # 替换值
# print(list_data[0][1])
for i in range(line):
    list_line = []  # 接收行
    for j in range(column):
        list_line.append(random.randint(0, 100))
    list_data.append(list_line)  # 将对应的行插入数组
print(f'未排序的结果:{list_data}')
# 进行排序操作(选用时间复杂度最低的冒牌排序)
for j in range(column):
    for i in range(line):
        for k in range(line - i - 1):
            if list_data[k][j] > list_data[k + 1][j]:
                temp = list_data[k][j]
                list_data[k][j] = list_data[k + 1][j]
                list_data[k + 1][j] = temp
print(f'排序后的结果(小到大):{list_data}')
# 第二种情况从小到大
import random

line = random.randint(1, 10)  # 行
column = random.randint(1, 10)  # 列
list_data = []
temp = 0  # 替换值
# print(list_data[0][1])
for i in range(line):
    list_line = []  # 接收行
    for j in range(column):
        list_line.append(random.randint(0, 100))
    list_data.append(list_line)  # 将对应的行插入数组
print(f'未排序的结果:{list_data}')
# 进行排序操作(选用时间复杂度最低的冒牌排序)
for j in range(column):
    for i in range(line):
        for k in range(line - i - 1):
            if list_data[k][j] < list_data[k + 1][j]:
                temp = list_data[k][j]
                list_data[k][j] = list_data[k + 1][j]
                list_data[k + 1][j] = temp
print(f'排序后的结果(大到小):{list_data}')

# 6有一个数据是A-Z,  第1个是A ，第26个是Z, 第27个变成A (从头开始) ，输入一个数字，判断所在位置的字母
# 第一种方法：
# chr()函数将ASCLL码转化为对应的字母
n = int(input('请输入一个正整数:'))
list_letter = []
for i in range(26):
    list_letter.append(chr(65 + i))
print(list_letter[n % 26 - 1])

# 7,一个有正有负的数组中，求出一个连续数字最大的个数个他们的和
# 如[1,2,3,4,100]最大连续个数为4（1，2，3，4）4个数据
#
continuous_value = 0
t = 0  # 最大的连续数
print_result = {'sum': 0, 'list_data': [], 't': 0}
list_tem = []
list_data = input('请以此输入数组：').split()
# list_data=[1,2,3,4,100]
list_data = list(map(int, list_data))
for i in range(len(list_data) - 1):
    # 因为连续的值可能有正有负数
    if list_data[i + 1] - list_data[i] == 1 or list_data[i + 1] - list_data[i] == -1:
        continuous_value = list_data[i + 1] - list_data[i]  # 获取连续值
    if list_data[i + 1] - list_data[i] == continuous_value:
        t += 1
        list_tem.append(list_data[i])
        list_tem.append(list_data[i + 1])
        if t > print_result['t']:  # 判断是否更新最新数据
            print_result['t'] = t
            print_result['list_data'] = list_tem
            print_result['sum'] = sum(print_result['list_data'])
    else:
        # 重置临时数据
        list_tem = []
        t = 0
# 利用集合去重
print_result['list_data'] = list(set(print_result['list_data']))
print(f"最大连续个数为{tuple(print_result['list_data'])}{len(print_result['list_data'])}个数据")
print(f"它们的和为:{print_result['sum']}")

# 8一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
#
t = 0  # 计数器
n = int(input('请输入一个整数n:'))
for i in range(n + 1):
    for j in range((n + 1) // 2):
        if i * 1 + j * 2 == n:
            t += 1
            # print(i, j)
print(t)

# 9，分红包  有n个人和s块钱，随机分配给n个人，每个人可以随机分配到多少钱？
import random

n, s = input('请按顺序输入人数和金钱：').split()
n, s = int(n), int(s)
sum_money = 10
money = []
t = 0  # 计数器
while True:
    money.append(random.randint(1, s))
    t += 1
    if sum(money) == s and len(money) == n:
        break
    if t > n:
        money = []
        t = 0
print(money)
