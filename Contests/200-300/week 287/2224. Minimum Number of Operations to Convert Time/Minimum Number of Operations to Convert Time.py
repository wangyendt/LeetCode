#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Convert Time.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_h, cur_m = current.split(':')
        cur = 60 * int(cur_h) + int(cur_m)
        cor_h, cor_m = correct.split(':')
        cor = 60 * int(cor_h) + int(cor_m)
        ret = 0
        tar = cor - cur
        m, d = divmod(tar, 60)
        ret += m
        m, d = divmod(d, 15)
        ret += m
        m, d = divmod(d, 5)
        ret += m
        ret += d
        return ret
