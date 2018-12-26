#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/20 0020下午 2:09


class A:
    def test(self):
        print('A.test')  # 2 执行这一步 打印
        super().f1()  # 3 然后在调用父类里的f1,   根据C.mro里的查找顺序执行到A 往后继续执行到B里去查找


class B:
    def f1(self):  # 4找到f1, 执行
        print('from B')  # 5打印


class C(A, B):
    pass


if __name__ == "__main__":
    # super（）会严格按照mro列表从当前查找到的位置继续往后查找
    c = C()
    print(C.mro())  # 调用属性的顺序  [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

    c.test()  # 1：C里没有 ，去A里调用
