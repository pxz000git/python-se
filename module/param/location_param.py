#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/26 0026上午 10:32


"""
可变参数
定义默认参数要牢记一点：默认参数必须指向不变对象！
"""


# 以下这个函数如果被 多次 调用会在默认添加多个END字符串
def add_end_0(l=[]):
    l.append('END')
    return l


# 为了避免这个问题，应该把传入的默认参数设置为不可变的
def add_end_1(l=None):
    l = []
    l.append('END')
    return l


if __name__ == "__main__":
    res = add_end_1()
    print(res)
