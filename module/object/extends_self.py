#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/8 0008下午 4:20

"""
继承中的self相关
self始终是原始调用的类的self
"""


class A(object):
    def a(self):
        print("A--a--self--%s" % self)


class B(A):
    def b(self):
        print("B--b--self--%s" % self)


if __name__ == "__main__":
    b_instance = B()
    b_instance.b()
    print("-----分割线----")
    b_instance.a()
