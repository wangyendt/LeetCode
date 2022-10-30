#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Thousand Separator.py 
@time: 2020/08/22
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        ret = []
        for i, a in enumerate(str(n)[::-1]):
            if i > 0 and i % 3 == 0:
                ret.append('.')
            ret.append(a)
        return ''.join(ret)[::-1]
