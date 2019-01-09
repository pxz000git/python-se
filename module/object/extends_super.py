#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/9 0009上午 11:49


"""
继承中的super相关
在python中，每个类都有一个mro的类方法。
这也是super在父类中查找成员的顺序
super在继承体系中向上的查找过程，变成了在mro中向右的线性查找过程，任何类都只会被处理一次
"""


# class Base(object):
#     def __init__(self):
#         print("Base init")
# 
# 
# class Leaf(Base):
#     """
#     Base直接父类调用
#     """
#     def __init__(self):
#         Base.__init__(self)
#         print("Leaf init")


# class Leaf(Base):
#     """
#     super调用
#     """
#     def __init__(self):
#         super(Leaf, self).__init__()
#         print("Leaf init")
#########################################


# class Base(object):
#     def __init__(self):
#         print("Base init")
# 
# 
# class Medium1(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Medium1 init")
# 
# 
# class Medium2(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Medium2 init")
# 
# 
# class Leaf(Medium1, Medium2):
#     def __init__(self):
#         Medium1.__init__(self)
#         Medium2.__init__(self)
#         print("Leaf init")
# ###################################################3

class Base(object):
    def __init__(self):
        print("Base init")


class Medium1(Base):
    def __init__(self):
        super(Medium1, self).__init__()
        print("Medium1 init")


class Medium2(Base):
    def __init__(self):
        super(Medium2, self).__init__()
        print("Medium2 init")


class Leaf(Medium1, Medium2):
    def __init__(self):
        super(Leaf, self).__init__()
        print("Leaf init")


if __name__ == "__main__":
    # leaf = Leaf()  # "Base init", "Leaf init"
    # ################
    # 可以看到Base被初始化了两次！这是由于Medium1和Medium2各自调用了Base的初始化函数导致的
    # 父类被多次初始化
    # leaf = Leaf()
    # 使用了super()
    # ################
    leaf = Leaf()
    '''
    Base init
    Medium2 init
    Medium1 init
    Leaf init
    '''
    print(Leaf.mro())
    '''
    [<class '__main__.Leaf'>, <class '__main__.Medium1'>, <class '__main__.Medium2'>, <class '__main__.Base'>, <class 'object'>]
    '''

