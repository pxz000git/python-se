#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/26 0026上午 10:40


"""
person_info:关键字参数
person_info2:命名关键字参数
"""


def person_info(name, age, **kw):
    """
    可变参数允许传入0个～多个参数，
    而关键字参数允许在调用时以字典形式传入0个或多个参数（注意区别，一个是字典一个是列表）；
    在传递参数时用等号（=）连接键和值
    """
    print("name", name, "age", age, "other", kw)


# 这里星号分割符后面的city、job是命名关键字参数
def person_info2(name, age, *, city, job):
    """
    命名关键字参数在关键字参数的基础上限制传入的的关键字的变量名
    * 和普通关键字参数不同，命名关键字参数需要一个用来区分的分隔符*，
    它后面的参数被认为是命名关键字参数
    """
    print(name, age, city, job)


# args是变长参数，而city和job是命名关键字参数
def person_info3(name, age, *args, city, job):
    """
    不过也有例外，如果参数中已经有一个可变参数的话，-> *args
    前面讲的星号分割符就不要写了（其实星号是写给Python解释器看的，
    如果一个星号也没有的话就无法区分命名关键字参数和位置参数了，
    而如果有一个星号即使来自变长参数就可以区分开来）
    """
    print(name, age, args, city)


if __name__ == "__main__":
    # 关键字参数
    # person_info("zhangsan", 18, city="beijing")

    # 命名关键字参数
    # 这里不再被自动组装为字典
    # person_info2("Alex", 17, city="Beijing", job="Engineer")

    # 这里可变参数依然会组装成元组传入
    person_info3("Liqiang", 43, "balabala", city="Wuhan", job="Coder")
    # Liqiang 43 ('balabala',) Wuhan
