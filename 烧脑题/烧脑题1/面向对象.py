# # 面向对象
# # 1.1
# # 问题:定义一个至少有两个方法的类:
# # getString:从控制台输入获取字符串
# # printString::打印大写字母的字符串。
# # 还请包含简单的测试函数来测试类方法。
# # 提示:使用_init__方法构造一些参数
# class ChangeBig:
#     def __init__(self):
#         char = self.getString()
#         self.printString(char)
#
#     def printString(self, char):
#         for i in char:
#             if i.isupper():
#                 print(i, end='')
#
#     def getString(self):
#         char = input('请输入字符串:')
#         return char
#
#
# if __name__ == '__main__':
#     w = ChangeBig()
