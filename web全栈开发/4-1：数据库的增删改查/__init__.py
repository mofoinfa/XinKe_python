# 家庭作业
# 1、数据库的发展分哪几个阶段？
# （1）人工管理阶段
# （2）文件系统阶段
# （3)数据库（管理）系统阶段

# 2、数据库的特点有哪些？
# 1. 实现数据共享：数据共享包含所有用户可同时存取数据库中的数据，也包括用户可以用各种方式通过接口使用数据库。
#
# 2. 减少数据的冗余度：同文件系统相比，由于数据库实现了数据共享，从而避免了用户各自建立应用文件。
#
# 3. 数据的独立性：数据的独立性包括数据库中数据库的逻辑结构和应用程序相互独立，也包括数据物理结构的变化不影响数据的逻辑结构。
#
# 4. 数据实现集中控制：文件管理方式中，数据处于一种分散的状态，不同的用户或同一用户在不同处理中其文件之间毫无关系。利用数据库
# 可对数据进行集中控制和管理，并通过数据模型表示各种数据的组织以及数据间的联系。
#
# 5. 数据一致性可维护性，以确保数据的安全性和可靠性
#
# 6. 故障恢复由数据库管理系统提供一套方法，可及时发现故障和修复故障，从而防止数据被破坏。
# 数据库系统能尽快恢复数据库系统运行时出现的故障，可能是物理上或是逻辑上的错误。比如对系统的误操作造成的数据错误等。

# 所学内容
# 一、数据库操作
# 1.创建数据库
# create database 数据库名;
# 2.删除数据库
# drop database 数据库名；
# 3.选择指定得数据库
# use 数据库名字
#
# 二、数据表操作
# 1.创建数据表
# create table 数据表名字（
#     id int auto_increment,#属性名：id，类型:int,功能：自增
#     title varchar(100) not null,#属性名：title，类型：carchar，功能：不为空
#     primary key(id)#将id设置为主键
# ）
# 2.查看所有数据表
# show table
# 3.删除数据表
# drop table 数据表名字
#
# 三、数据操作
# 1.插入数据
# insert into 表名 (表头，表头) values (数据，数据)
#
# 2.更新数据
# update 表明 set 表头='数据' where 标头='数据'
#
# 3.删除数据
# delete from 表名 where 标头='数据'
#
# 4.数据查询
# select 表头，表头 from 表名 where 标头='数据' #单独查询
# select * from 表名 #查询表的所有数据

