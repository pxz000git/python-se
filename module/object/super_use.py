#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/9 0009下午 12:16


"""
super的具体用法
super() 同super(class, obj)=super(type, obj)
super(type, obj)
super(type)
super(type, type1)

super(Leaf, self).__init__()的意思是说：

获取self所属类的mro, 也就是[Leaf, Medium1, Medium2, Base]
从mro中Leaf右边的一个类开始，依次寻找__init__函数。这里是从Medium1开始寻找
一旦找到，就把找到的__init__函数绑定到self对象，并返回

super(Type, self).__init__()
意义是：
    super(E, self).__init__()
    1、获取self所属类的mro, 也就是[E, B, C, D, A]
    2、从mro中E右边的一个类开始，依次寻找__init__函数。这里是从B开始寻找
    2-1、找到B时:super(B, self).__init__(),此时self仍然是E的对象，获取self所属类的mro,也就是[E, B, C, D, A]
        从mro中B右边的一个类开始，依次寻找__init__函数。这里是从C开始寻找
    3、一旦找到，就把找到的__init__函数绑定到self对象，并返回
"""


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


class A:
    def __init__(self):
        print("Enter A")
        print("Leave A")


class B(A):
    def __init__(self):
        print("Enter B")
        super(B, self).__init__()
        print("Leave B")


class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leave C")


class D(A):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leave D")


class E(B, C, D):
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leave E")


if __name__ == "__main__":
    """
    从这个执行流程可以看到，如果我们不想调用Medium1的__init__，
    而想要调用Medium2的__init__，那么super应该写成：super(Medium1, self)__init__()
    """
    print(Leaf.mro())
    leaf = Leaf()

    # E()
    # print(E.mro())
    '''
    Enter E
    Enter B
    Enter C
    Enter D
    Enter A
    Leave A
    Leave D
    Leave C
    Leave B
    Leave E
    '''
