#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: API_utils.py 
@time: 2020/04/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class DataStructureProblem:
    def __init__(self, p_order, p_params):
        self.order = p_order
        self.params = p_params

    def get_result(self):
        assert len(self.order) == len(self.params) > 0
        obj = eval(f'{self.order[0]}(*{self.params[0]})')
        for i, (o, p) in enumerate(zip(self.order, self.params)):
            if i > 0:
                yield getattr(obj, o)(*p)

    def print(self):
        for res in self.get_result():
            if res:
                print(res, end=',')
            else:
                print('null', end=',')


def call_me(class_, callers, params):
    cls = None
    my_class = class_
    for func, param in zip(callers, params):
        if func == my_class.__name__:
            cls = my_class(*param)
            print('null', end=',')
        else:
            res = cls.__getattribute__(func)(*param)
            prt = res if res else 'null'
            print(prt, end=',')
