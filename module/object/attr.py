#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/20 0020下午 1:42


class AttrHasTest(object):
    name = "test"

    def run(self):
        return "Hello"


class AttrGetTest(object):
    name = "test"

    def run(self):
        return "Hello"


class AttrSetTest(object):
    name = "test"

    def run(self):
        return "Hello"


if __name__ == "__main__":
    # ========================hasattr===========================
    # 判断attr这个对象是否有name属性，返回值为bool
    '''
    attr = AttrHasTest()
    b = hasattr(attr, "name")
    print("the value of b is %s" % b) 
    '''
    # ========================getattr===========================
    # 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
    # 需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
    # 可以在后面添加一对括号
    '''
    attr = AttrGetTest()
    print(getattr(attr, "name", ))
    print(getattr(attr, "run"))
    # 返回方法的内存地址
    print(getattr(attr, "run")())
    # 不存在的属性就报错
    # print(getattr(attr, "age"))

    # 不存在，返回默认值
    print(getattr(attr, "age", 18))
    if attr.run() == "a":
        print(getattr(attr, attr.run(), 19))
    else:
        print(getattr(attr, attr.run(), 20))
    '''
    # ====================setattr===============================
    # 给对象的属性赋值，若属性不存在，先创建再赋值。
    '''
    attr = AttrSetTest()
    if hasattr(attr, 'name'):
        setattr(attr, 'age', 21)
        print(getattr(attr, 'age'))
    else:
        setattr(attr, 'age', 22)
        print(getattr(attr, 'age'))
    '''
    # 一种综合的用法是：判断一个对象的属性是否存在，若不存在就添加该属性。
