#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Check If It Is a Good Array
@time: 2019/11/8 15:26
"""


class Solution:
    def isGoodArray(self, A):
        gcd = A[0]
        for a in A:
            while a:
                gcd, a = a, gcd % a
        return gcd == 1