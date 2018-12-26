#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/26 0026上午 10:35


"""
可变参数
"""


# 传入一个列表，严格地说这不是可变参数
def calc(l):
    sum = 0
    for n in l:
        sum += n
    return sum


# 这才是可变参数，虽然在使用上和列表没有区别，
# 但是参数nums接收到的是一个tuple（这些参数在传入时被自动组组装为一个元祖）
def calc_ch(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


if __name__ == "__main__":
    # res = calc([1, 2, 3])
    # print(res)
    # res = calc_ch(1, 2, 3)
    # print(res)
    my_ls = [1, 2, 3]
    res2 = calc_ch(*my_ls)
    print(res2)
