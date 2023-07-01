# 家庭作业
# 用正则表达式匹配一个身份证号
# 要求判断 :长度是18  前17位是数字  第18位是数字或者X
# import re
#
# idCard = input('请输入你的身份证号:')
# re_data = re.compile('\d{17}[0-9X]')
# # print(re_data.findall(idCard))
# if re_data.match(idCard):
#     print('成功匹配到身份证号')
# else:
#     print('这是一个无效的身份证号')

# 所学内容
# 一、正则表达式的调用
import re

# 二、常用方法
# 1.判断数据是否是需要的数据自带
# str_data = '123ccc321 123aaa321'
# data = re.match('123', str_data)
# print(data)  # 有的话返回对应数据对象，没有返回none
# 2.在数据中查找
# str_data = '123ccc321 123aaa321'
# data = re.search('123', str_data)
# print(data)  # ，有就返回数据对象，没有就返回none
# 3.返回所需要的数据文本-(findall(所需要的数据,数据集))
# str_data = '123ccc321 123aaa321'
# data=re.findall('123',str_data)
# 4.进行一个总的分类，可以直接调用数据，让表达式可以重复多次使用-（compile（需要的数据））
# re_data=re.compile('abc')
# re_data.match()#查找
# re_data.search()#搜素
# re_data.findall()#查找

# 三、元字符
# 1.输出所学范围-（()）
# str_data = '123ccc321 123aaa321'
# print(re.findall('3(...)3', str_data))#输出两个3之间的三个数据
# 2.通配符(.)-除了\n不能匹配外，其它全部都能匹配，一个点代表一个字符
# str_data = '123ccc321 123aaa321'
# print(re.findall('3(...)3', str_data))#输出两个3之间的三个数据
# 3.开头符(^)-只能放在数据的最前面
# str_data = '123ccc321 123aaa321'
# print(re.findall('^12', str_data))#输出最前面两个数据
# 4.结尾符($)-只能放在数据的最后
# str_data = '123ccc321 123aaa321'
# print(re.findall('321$', str_data))#输出最前面两个数据
# # 5.获取数字与非数字(\d)
# str_data = '123ccc321 123aaa321'
# print(re.findall('^\d\d', str_data))  # 输出最前面两个数字数据
# 补集:print(re.findall('(\D\D\D)321$', str_data))  # 输出末尾321前面的三个非数字数据
# 6.匹配任何空白字符(\s)
# str_data = 'abc\t\t\tabc  abc\n\n\nabc abc123abc'
# print(re.findall('^abc(\s\s\s)', str_data))  # 获取abc后的三个空白字符
# 补集:print(re.findall('^\S\S\S', str_data))  # 获取前三个非空白字符
# 7. 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。下划线也可以匹配到(\w)
# str_data = 'abc\t\t\tabc  abc\n\n\nabc abc123abc'
# print(re.findall('\w\w\w\w$', str_data))  # 获取后四个数字字母字符集
# 补集:print(re.findall('^abc(\W\W\W)', str_data))  # 获取abc后的三个非数字字母字符集
# 8.代表获取数据数量({})--里面只能是数字
# str_data = 'abc\t\t\tabc  abc\n\n\nabc abc123abc'
# print(re.findall('^\w{3}', str_data))  # 获取前三个字符
# 深意：{1，3}表示获取1-3的数据
# 9.选择获取的数据类型([])--以或的形式呈现
# str_data = 'a3bc\t\t\tabc  abc\n\n\nabc abc123abc'
# print(re.findall('^[a1-5]{1,3}', str_data))  # 获第一个字符a和第二个数字3
# 10.代表0-无穷次(*)
# str_data = 'abc\t\t\tabc  abcXXXabc abc123abc'
# print(re.findall('c(.*)a', str_data))  # 获第一个c和最后一个a之间的所有数据
# 11.代表1次到无穷次(+)
# str_data = 'a1234567b89'
# print(re.findall('a(\d+)', str_data))  # 获取a后到b之前所有的数字
# 12.代表0次到1次(?)
# str_data = 'a1234567b89'
# print(re.findall('^(a1?)', str_data))  # 获取前两个数据
# 综上：{0,} == *，{1,} == +，{0,1} == ？

# 13.*? 惰性匹配 .*贪婪匹配
# 惰性匹配--没满足条件就输出结果，进行下一轮搜索
# str_data = 'abc\t\t\tabc  abcXXXabc abc123abc'
# print(re.findall('c(.*?)a', str_data))  # 获取每一个c和a之间的数据
# 贪婪匹配--找第一个和最后一个满足的条件，输出所有其间的数据
# str_data = 'abc\t\t\tabc  abcXXXabc abc123abc'
# print(re.findall('c(.*)a', str_data))  # 获第一个c和最后一个a之间的所有数据

# 14.换行
# re.S 匹配换行  正则匹配不能换行
# '1234'
# '56789'
# '1234567'
# '0000000'
# 可以
# 56789  0000000
# 需要re.S
# 1234 56789    0000000  re.S


# 注意--当字符内出现转义字符时可以用取消转义符进行数据的获取
import re
# a = '^123^'
# print(re.findall('^(\d+)^', a))
# print(re.findall('\^(\d+)\^', a))
