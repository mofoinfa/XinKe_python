# 家庭作业
# 1、自己分别写一个，一对一、一对多、多对多的案例（截图模型类的代码）
# 2、简单使用一下 F 对象查询（截图代码+效果）

# 所学内容
# 一、数据表关联映射（一对一、一对多、多对多）
# 1.一对一
# 介绍：比较少用，是指一个表对另外一个表信息的补充，比如一个表是书籍，另外则是书籍详情
# 代码：
# class A(model.Model):
#     A_id=models.AutoField(primary_key=True)
# class B(model.Model):
#     B_id = models.ForeignKey(多对一中"一"的模型类, ...)
#
# 2.一对多
# 介绍：主要为了减少冗余，像教师有多个部门，那教师表里的部门可以作为教师表的一个外键表
# 代码：
#     class A(model.Model):
#         A_id=models.AutoField(primary_key=True)
#     class B(model.Model):
#         B_id=models.AutoField(primary_key=True)
#         pub = models.ForeignKey(to=A, on_delete=models.CASCADE, null=True)
#         # 创建B外键关联pub,与A_id（A表主键）关联
#
# 3.多对多
# 介绍：常用来表示表与表的关联，例如老师带的学生的对应关系
#     class A(model.Model):
#         A_id=models.AutoField(primary_key=True)
#     class B(model.Model):
#         B_id=models.AutoField(primary_key=True)
#         pub = models.ForeignKey(to=A, on_delete=models.CASCADE, null=True)
#     class C(model.Model):
#         C_id=models.AutoField(primary_key=True)
#         A=ManyToManyField(A)#关联A表主键
#         B=ManyToManyField(B)#关联B表主键
