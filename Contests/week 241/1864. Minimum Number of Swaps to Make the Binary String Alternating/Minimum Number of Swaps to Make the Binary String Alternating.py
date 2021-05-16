#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Swaps to Make the Binary String Alternating.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        n0 = sum(1 for t in s if t == '0')
        n1 = n - n0
        if abs(n0 - n1) > 1:
            return -1
        ret = n
        if n & 1:
            if n1 > n0:
                target = '10' * (n // 2) + '1'
            else:
                target = '01' * (n // 2) + '0'
            res = 0
            for i in range(n):
                if s[i] != target[i]:
                    res += 1
            ret = min(ret, res // 2)
        else:
            for target in ('10' * (n // 2), '01' * (n // 2)):
                res = 0
                for i in range(n):
                    if s[i] != target[i]:
                        res += 1
                ret = min(ret, res // 2)
        return ret
