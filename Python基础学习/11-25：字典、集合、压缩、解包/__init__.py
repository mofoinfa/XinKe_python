# 家庭作业
# 本次考试张三59分, 李四80, 王五99分, 小宋56分, 请使用字典来 表达此数据结构, 并筛选出来不及格的同学及分数
# dict_point = {'张三': 59, '李四': 80, '王五': 99, '小宋': 56}
# for i in dict_point:
#     if dict_point[i] < 60:
#         print(f'{i}同学不及格，分数是:{dict_point[i]}分')

# 所学内容
# 一、字典（可变数据类型）--dict
# 1.
# 格式：dict_data = {key: value}
# 2.
# 注意：key的数据必须是不可变类型，且key的数据是不可重复的
# 3.
# 字典定义
# 1）dict_data = {}  # 定义空字典
# 2）dict_data = {'小明': 18}  # 定义单字典
# 3）dict_data = {'小明': {'age': 20, 'sex': 'mel'}, '小王'{'age': 18, 'sex': 19}}
# 4.
# 输出字典
# dict_data = {'小明': {'age': 20, 'sex': 'mel'}, '小王'{'age': 18, 'sex': 19}}
# print(dict_data['小明']['age'])  # 根据键值输出对应的内容
# 5.
# 增加新的键值
# dict_data = {}  # 定义空字典
# # 增加第一个
# dict_data = {'小明': 20}
# dict_data['小王'] = {'age': 18, 'sex': 'male'}
# print(dict_data)
# 6.字典修改
# 字典修改 当key重复的时候，后面进来的数据会覆盖前面的数据
# dict_data = {'小明': 20}
# dict_data['小明'] = 18
# print(dict_data)
# eg:当数据不存在就增加 当数据存在就修改
# 7.字典删除
# dict_data = {'小明': 20}
# del dict_data['小明']

# 二、字典的方法
# dict_data = {'小刚': {'age': 20}, '小明': 20}  # 数据
# 1.pop
# 写法：dict_data.pop('小明')#利用key值删除字典

# 2.popitem
# 写法：dict_data.popitem()#删除字典的最后一个数据

# 3.update
# 1）写法：dict_data.update({'小明':18})
# 2）写法：dict_data['小明']=18

# 4.keys() # 获取字典中的所有key 存放到一个dict_keys对象里面
# 写法：
# for i in dict_data.keys():
#     print(i)

# 5.values() #获取字典中的所有value
# 写法：
# for i in dict_data.values():
#     print(i)

# 6.# items() 获取字典内的所有数据并将每一个元素化为一个模块
# 写法1：
# for i in dict_data.items():
#     print(i[0], i[1])
# 写法2：
# for name, age in dict_data.items():#利用解包和压缩的思想
#     print(f'name:{name} age:{age}')

# 三、压缩与解包
# 1.压缩
# a = 1, '小明'
# print(a)
# 2.解包
# age, name = a
# print(name,age)
# 3.扩展，二维数组的解包
# 依次输出每个数组内的元素
# dict_data = [[1, 2], [3, 4]]
# for i, j in dict_data:
#     print(i, j)

# 四、集合
# 1.定义
# 1)set_data={1,2}
# 2)set_data=set(1,2)
# 2.特点
#  set_data = {数据,数据,数据,数据,......}  数据结构
#  无序的 , 唯一的(数据不能重复)
#  集合没有索引和key
# 3.方法
# 1）add  # 向末尾添加一个数字
# set_data.add(100)
# print(set_data)
# 2）remove#根据数据删除对应的数据
# set_data.remove('0')
# print(set_data)
# 4.扩展可以用于元素的去重
# list_data = [1, 2, 1, 2, 3, 4, 5, 8, 100, 2]
# # 想要得到不重复的数字
# set_data = set(list_data)
# print(f'集合:{set_data}')
# # 最后可以重新转化为数组
# list_data = list(set_data)
# print(f'列表:{list_data}')
