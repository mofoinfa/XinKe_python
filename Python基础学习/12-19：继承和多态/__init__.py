# 家庭作业
# 1）用面向对象的形式编写一个老师类与学生
# 老师有特征：编号、姓名、性别、年龄、等级、工资，老师类中有功能 可以改作业、上课。
# 学生有特征：学号、姓名、性别、年龄、成绩，学生类中有功能 可以上课、完成作业。
# 2）要求写一个基础的类  老师和学生类来继承他 ，用于去除重复的特征和功能
class People:
    name = ''
    gender = ''
    age = ''

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Teacher(People):
    tid = 0
    level = ''
    salary = 0

    def __init__(self, name, gender, age, tid, level, salary):
        super(Teacher, self).__init__(name, gender, age)
        self.level = level
        self.salary = salary
        self.tid = tid

    def change_homework(self):
        print(f'{self.name}正在批改作业')

    def attendClass(self):
        print(f'{self.name}正在上课')

    def get_info(self):
        print('-' * 10, '个人信息', '-' * 10)
        print('身份：老师')
        print(f'编号：{self.tid}')
        print(f'姓名：{self.name}')
        print(f'性别：{self.gender}')
        print(f'年龄：{self.age}')
        print(f'级别：{self.level}')
        print(f'工资：{self.salary}/每月')


class Student(People):
    sid = 0
    grade = 0

    def __init__(self, name, gender, sid, age, grade):
        super(Student, self).__init__(name, gender, age)
        self.grade = grade
        self.sid = sid

    def listen_class(self):
        print(f'{self.name}同学正在听课')

    def complete_homework(self):
        print(f'{self.name}同学正在完成作业')

    def get_info(self):
        print('-' * 10, '个人信息', '-' * 10)
        print('身份：学生')
        print(f'姓名：{self.name}')
        print(f'学号：{self.sid}')
        print(f'性别：{self.gender}')
        print(f'年龄：{self.age}')
        print(f'成绩：{self.grade}分')


# 初始化
teacher = Teacher('王老师', '男', 22, 1, '高级', 5000)
student = Student('张三', '男', 10001, 14, 85)

# 输出老师的功能
teacher.get_info()
teacher.attendClass()
teacher.change_homework()

# 输出学生的功能
student.get_info()
student.listen_class()
student.complete_homework()

# 所学内容：
# 一、继承
# 1.一个类可以被多个类继承
#
#
# class C:
#     pass
#
#
# class A(C):
#     pass
#
#
# class B(C):
#     pass
# 2.子类和父类的初始化方法
# 注意：super指调用父类对象
# class A():
#     def __init__(self, name):
#         self.name = name
#
#
# class B(A):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
# 二、多态
# 多个从不同方向的继承组成多态
