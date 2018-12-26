#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/25 0025下午 5:28


# class SuperClass(object):
#     def act(self):
#         print("Super Class act method ...")
#
#
# class SubClass(SuperClass):
#     def act(self):
#         super
#         SuperClass.act(self)        # 显式地调用父类方法
#         print("SubClass act method ...")
# class SuperClass(object):
#     def act(self):
#         print("Super Class act method ...")
#
#
# class SubClass(SuperClass):
#     def act(self):
#         super().act()
#         # super(SubClass,self).act()     # py2.x 调用父类，过于复杂，这个可以正常执行
#         print("SubClass act method ...")
# class A(object):
#     def act(self):
#         print("call A act method ....")
#
#
# class B(object):
#     def act(self):
#         print("call B act method ....")
#
#
# class C(B, A):  # 搜索的顺序会从B开始搜索，B存在act方法则调用并返回，不再继续搜索
#     def act(self):
#         super().act()
# class E(object):
#     '''
#     这个 魔法函数如果放在 类里面， 会直接找 Person属性，
#     item会自增加 直到找不到报错结束， 使用的时候 直接 类的实例 做for循环，
#     就可以了， 不需要用 实例再调用属性，因为魔法函数已经替你完成了这一步
#     '''
#     def __getitem__(self, item):
#         print("call E __getitem__ method ...")
#
#
# class F(E):
#     def __getitem__(self, item):
#         print('call F __getitem__ method ..')
#         E.__getitem__(self, item)
#         super().__getitem__(item)
#         super()[item]  # 不支持运算符操作，'super' object is not subscriptable
#
#
# def test_opr():
#     f = F()
#     f[2]
# class X(object):
#     def m1(self):
#         print("call X method")
#
#
# class Y(object):
#     def m1(self):
#         print("call Y method")
#
#
# class Z(X):
#     def m1(self):
#         super().m1()
#
#
# def test_z():
#     # 在Python中，每个类有一个__bases__属性，列出其基类
#     z = Z()
#     z.m1()
#     print("change Z class base for Y ....")
#     Z.__bases__ = (Y,)
#     z.m1()
class IA(object):
    def __init__(self):
        print("call IA init ...")  # 基类IA没有super()，没有意义


class IB(IA):
    def __init__(self):
        print("call IB init ....")
        super().__init__()


class IC(IA):
    def __init__(self):
        print("call IC init ....")
        super().__init__()


class ID(IC, IB):
    def __init__(self):
        print("call ID init ...")
        super().__init__()


def test_ID():
    d = ID()
    print(ID.mro())


if __name__ == '__main__':
    # sub = SubClass()
    # print(SubClass.mro())
    # sub.act()

    # sub = SubClass()
    # sub.act()

    # c = C()
    # c.act()

    # test_opr()

    # test_z()

    # 能够在多继承中按照广度优先的继承树搜索关系链来有序地调用与父类相同名称的方法，
    # 且在每个子类拥有super的都会执行父类方法
    # test_ID()
    pass


