# import random
#
# a = random.randint(1, 10)
# print(a)
#
# # 代码推断
#
# # 变量
# var_1: int = 10  # 变量后面跟冒号和要注解的类型
#
# #
# # 函数  方法
# #
# # 形参
# def add(x: int, y: int):
#     return x + y
# print(add(1,2))
#
#
# class Student():
#     pass
#
#
# stu: Student = Student()  # 类对象注解
#
# # 数据容器
#
#
# my_list: list = [1, 2, 3]  # 数据容器注解
#
# # 详细注解
# #  比如列表 内的数据进行注解就是详细注解  全部用中括号
# my_list: list[int] = [1, 2, 3]
#
# my_dict: dict[str, int] = {'dad': 1}
#
#
#
# def func(date:list) -> list:  # 返回值注解 ->括号冒号中间
#     return list
#
#
# # Union


from typing import Union

# 混合类型注解  比如列表里有多种类型

my_list: list[Union[list, str, int]] = ["sada", 1, ["das", 564], ]
# Union  后跟[]

my_list()
my_list2: Union[list, str] = ["sada", 1, ["das", 564]]
my_list()
