# 家庭作业
# 将一个字符‘hello world’, 将l使用a替换后, 并将所有o删掉,请将程序结果打印出来
# 结果应该为：heaa wrad
char = 'hello world'
char = char.replace('l', 'a', char.count('l'))  # 查找所有l的全部个数，并进行替换
char = char.replace('o', '', char.count('o'))  # 查找所有的o，并进行替换
print(char)

# 所学内容
# 一、字符串
# 正负索引
# char ='abcdfe'
# 正索引：[0,1,2,3,4,5]
# 负索引：[-6,-5,-4,-3,-2,-1]

# 二、切片
# 1）格式：
# [第一刀；第二刀：步长]#步长默认为1,
# 例题,切除字符串cd
# char ='abcdfe'
# 以此为例将此进行切片划分为：[ |a|b|c|d|e|f|],下方为对应的刀数
# ####################: [ 0 1 2 3 4 5 6]
# cd=char[2:4]
# 例题,切除字符串ce
# ce=char[2:5:2]
# 2）步长：切片完后默认取值的顺序
# 倒置：char的字符取反
# char=char[::-1]

# 三、方法
# 1）join
# 写法：' '.join(str)#每一个字符串中间加入空格
# 2）replace
# 写法：str.replace('被替换字符','将替换字符','替换字符个数')
# 3）split
# 写法：str.split()#根据字符串存在的该字符进行分裂，存入分裂后的数字，默认为空
# 4）splitlines
# 写法：str.splitlines()  # 默认对\n进行分割
# 5）strip()
# 写法：
# str = '  \r \t \n  hello world  \r \t \n  '
# str.strip()  # 返回字符串的剪裁版本 去除字符串两边的空白符 \r \t \n。
# 6）upper()
# 写法：str.upper()#把字符串转换为大写。
# 7）lower()
# 写法：str.lower()#把字符串转换为小写。
# lower()	把字符串转换为小写。
# 8）count（）
# 写法：str.count(b)#统计b字符串在str字符串中出现了几次
# 9）find()、index()
# str.find('b')、str.index('b')#输出b字符串在str出现的的下标索引，find没有输出-1，index则报错
