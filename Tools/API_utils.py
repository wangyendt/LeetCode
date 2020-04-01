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


def call_me(class_, callers, params):
    cls = None
    my_class = class_
    for func, param in zip(callers, params):
        if func == my_class.__name__:
            cls = my_class(*param)
        else:
            print(cls.__getattribute__(func)(*param), end=' ')
