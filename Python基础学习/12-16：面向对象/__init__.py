# 家庭作业
# 1）定义名为MyTime（我的时间）的类
# 2）其中应有三个实例变量 时hour  分minute  秒second
# 3）对时分秒进行初始化，写入__init__()中
# 4)   定义方法get和set方法，get方法获取时间，set可以设置时间
# 5)   调用set设置一个时间  调用get输出时间

# import datetime
# import pygame
#
# # FPS（每秒帧数）控制器
# fps = pygame.time.Clock()
#
#
# class MyTime:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def set(self):
#         str_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         str_date = str_date.replace('-', ' ', str_date.count('-'))
#         str_date = str_date.replace(':', ' ', str_date.count(':'))
#         list_date = list(map(int, str_date.split()))
#         self.hour = list_date[3]
#         self.minute = list_date[4]
#         self.second = list_date[5]
#
#     def get(self):
#         print(f'北京时间 {self.hour}:{self.minute}:{self.second}')
#
#
# date = MyTime(0, 0, 0)
# date.set()
# while True:
#     date.set()
#     date.get()
#     fps.tick(1)


# 所学内容
# 一、魔法方法
# 定义：被动满足某种条件，被触发
class Washer:
    h = 850
    w = 460

    def __init__(self, name, color):  # 初始化  当对象被创建的时候自动运行
        self.name = name
        self.color = color

    def laundry(self):  # self 对象本身
        print('我会洗衣服')

    def __str__(self):
        return f'洗衣机的名称叫{self.name}'

    def __add__(self, other):
        return self.h + other.h

    def __len__(self):
        return self.w


haier = Washer('haier', 'red')  # 调用了 def __add__(self, other)
print(haier.color)  # 调用了  def __str__(self)
