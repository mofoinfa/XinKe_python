# # 家庭作业
# # 1、创建一个data.txt的文件
# # 2、用文件的写的方法往里面写上一首诗，并输出里面的全部内容
# # 静夜思
# # 唐代：李白
# # 床前明月光，疑是地上霜。
# # 举头望明月，低头思故乡。
# # 3、删除最后一行的诗句后并输出删除后的内容
#
# # 第一种方法（较复杂）
# # 创建文件存入古诗
# f = open(file='data.file', mode='w+', encoding='utf-8')
# f.write('静夜思\n'
#         '唐代:李白\n'
#         '床前明月光，疑是地上霜。\n'
#         '举头望明月，低头思故乡。\n'
#         )
# f.seek(0)
# print(f.read())
# f.close()
# # 读出古诗
# f = open(file='data.file', mode='r', encoding='utf-8')
# # print(f'输出完整古诗：\n{f.read()}')
# f.seek(0)  # 光标重新定位至0
# list_poetry = f.readlines()
# f.close()
#
# list_poetry.pop()  # 删除古诗的最后一行
#
# f = open(file='data.file', mode='w', encoding='utf-8')
# f.writelines(list_poetry)
# f.close()
#
# f = open(file='data.file', mode='r', encoding='utf-8')
# print(f'\n{f.read()}')
# f.close()
#
#
# 第二种方法（函数优化）
# def r_file():
#     f = open(file='data.file', mode='r', encoding='utf-8')
#     print(f'输出古诗：\n{f.read()}')
#     f.seek(0)  # 光标重新定位至0
#     list_poetry = f.readlines()
#     f.close()
#     return list_poetry
#
#
# def w_file(data):
#     f = open(file='data.file', mode='w', encoding='utf-8')
#     if isinstance(data, str):
#         f.write(data)
#     else:
#         f.writelines(data)
#     f.close()
#
#
# w_file('静夜思\n'
#        '唐代:李白\n'
#        '床前明月光，疑是地上霜。\n'
#        '举头望明月，低头思故乡。\n')
# list_poetry = r_file()
# list_poetry.pop()  # 删除最后一行
# w_file(list_poetry)
# r_file()

# # 所学内容
# 一、文件操作
# 定义：f=open(file='文件地址',mode='模式',encoding='版本')
# 1.文件地址
# （1）绝对地址：该文件相对于计算机的位置，例如：F:\python_project2206\day15-文件操作\data.txt
# （2）相对位置：该文件相当于此前文件的位置：
#     同一级：data.txt
#     下一级：next/new.txt
#     上一级：../12-14第十六节课/new.txt
#
# 2.模式
# （1）r：进行读操作
# 例如：
# f = open(file='data.txt', mode='r', encoding='utf-8')
# print(f.read())  # 读取所有的内容
# f.seek(0)  # 移动光标到指定位置
# print(f.read())  # 数据已经被读取，光标移动到最后
# f.close()
# （2）w：进行写操作（会清除之前文件内的所有内容）
# f = open(file='data.txt', mode='w', encoding='utf-8')
# f.write('python\n')
# f.write('文件操作')
# f.close()
# （3）a：追加（光标自动定位到末尾进行书写）
# f = open(file='data.txt', mode='a', encoding='utf-8')
# f.write('\npython\n')
# f.write('文件操作')
# f.close()
#
# 3.版本
# 一般通用utf-8
#
# 4.文件使用方法
# （1）f.seek():调整光标的位置--f.seek(0)将光标的位置调整至0
# （2）f.readlines():将每行读取的数据进行读取，最后返回一个列表
# （3）f.writelines(list):将列表里面的数据存入文件内
# 例如：修改一个数据
# f = open(file='data.txt', mode='r', encoding='utf-8')
# file_data = f.readlines()
# f.close()
#
# file_data[2] = '你好\n'  # 修改列表的第三个内容  替换内容 ''
#
# f = open(file='data.txt', mode='w', encoding='utf-8')
# f.writelines(file_data)
# f.close()
#
# 二、os和shutil模块操作文件
# import os
# 1.os.getcwd()	获取当前路径
# 2.os.rename(老的路径，新的路径)	重命名文件或者文件夹
# eg:相对路径修改--os.rename(r'data_file.txt', r'data.txt')
# 3.os.remove(文件所在的路径):删除文件
# 4.os.mkdir(r'F:\python_project2206\day15-文件操作\demo')创建文件夹  只能创建一个文件夹 一个一个文件夹的创建
# 5.os.makedirs():创建整个路径
# 6.os.rmdir():删除文件夹 只能删除空的文件夹
# import shutil
# 1.shutil.rmtree('text'):可以把文件和内容全部删除
# 2.shutil.copy('复制的位置', '复制的文件'):复制文件 修改文件位置和名称
# eg:
# import shutil
# shutil.copy('../12-14第十六节课/', 'new.txt')
