#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/20 0020下午 2:39




class A:
    a = "1"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def proce(para):
    print(para)


class B(A):
    def p(self):
        proce(self.a)


if __name__ == "__main__":
    b = B()
    b.p()
