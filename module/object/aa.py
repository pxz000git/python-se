#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/20 0020下午 2:39


class A(object):
    def a(self):
        ret = getattr(self, 'b')
        return ret()

    def b(self):
        # pass
        # print('b')
        return 'c'


if __name__ == "__main__":
    d = A().a()
    print(d)
    print(type(d))

