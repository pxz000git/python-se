#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/26 0026上午 10:53


"""
参数组合
    总结一下，在Python中一种可以使用5中传递参数的方式
    （位置参数、默认参数、变长参数、关键字参数、命名关键字参数）
    注意，这些参数在书写时要遵循一定的顺序即：
        位置参数、默认参数、变长参数、关键字参数、命名关键字参数（和本文的行文顺序一致）
"""


def f1(a, b, c=0, *args, **kw):
    print("args = ", args[0], ", kw = ", kw.get('x', 100))

    print("a = ", a, ", b = ", b, ", c = ", c, ", args = ", args, ", kw = ", kw)


def f2(a, b, c=0, *, d, **kw):
    print("a = ", a, ", b = ", b, ", c = ", c, ", d = ", d, ", kw = ", kw)


if __name__ == "__main__":
    # f1(1, 2)  # a =  1 , b =  2 , c =  0 , args =  () , kw =  {}
    # f1(1, 2, c=3)  # a =  1 , b =  2 , c =  3 , args =  () , kw =  {}
    f1(1, 2, 3, 'a', 'b')  # a =  1 , b =  2 , c =  3 , args =  ('a', 'b') , kw =  {}
    f1(1, 2, 3, 'a', 'b', x=99)  # a =  1 , b =  2 , c =  3 , args =  ('a', 'b') , kw =  {'x': 99}
    f2(1, 2, d=99, ext=None)  # a =  1 , b =  2 , c =  0 , d =  99 , kw =  {'ext': None}
