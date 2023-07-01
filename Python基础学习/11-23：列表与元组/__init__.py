# 家庭作业
# 1,办公室里有张三, 李四, 王五3个人, 现在小宋也到班公室来上班了,如何用列表来表示?并输出办公室有哪些人;
# 2,过了一会, 王五有事离开了办公室, 程序应该如何表达?并输出办公室有哪些人
list_person = ['张三', '李四', '王五']
list_person.append('小宋')  # 小宋来到办公室上班了
print(f'人数第一次变更:{list_person}')
list_person.remove('王五')  # 王五有事离开办公室
print(f'人数第二次变更:{list_person}')

# 课堂所学
# 一、列表的定义以及比较字符串
# name = ['天', '下', '号', '你']
# name.sort()
# name.extend('12345')
# print(id(name[0]))
# 二、列表常规操作
# list_data=[]
# 1）append
# list_data.append('1')#向列表内添加字符串1
# 2）pop
# list_data.pop(0)#根据索引进行删除，默认删除最后一个
# 3）sort
# list_data.sort()#对列表进行排序，若想倒叙可在括号内输入list_data.sort(reverse=True)
# 4)reverse
# list_data.reverse()#倒置，将列表内的数字进行倒置
# 5）count
# list_data.count('b')#判断b在数列中出现的次数
# 6）index
# list_data.index('b')#查找b字符串在改列表的下标
# 7）extend
# list_data.extend()#添加多个元素进入字符串，可以选择不同类型（+号只能添加相同的类型）
# 8）remove
# list_data.remove('b')#删除列表内元素为b的元素
# 9）insert
# list_data.insert(0,'a')#向0索引的位置插入a的元素
# 10）clear
# list_data.clear()#情况列表中的数据
# 11）copy
# list_data1=list_data.copy()#创建一个新的数组，该数组中元素为复制的值
# 三、元组
# 与列表的区别：1）不可更改数据
#            2）为小括号
#            3）tuple_data = (1,)，data = (1)  # 如果不加，就相当于没有括号
# 四、公共方法
# len() 获取容器里面的长度
# print(len('12345'))
# print(len([1, 2, 3]))
#
# del   删除变量
# list1 = [1, 2, 3]
# # del(list1[0])
# del list1[0]
# print(list1)
