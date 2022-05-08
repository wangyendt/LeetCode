#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest 3-Same-Digit Number in String.py 
@time: 2022/05/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        res = []
        for i in range(2, n):
            if num[i] == num[i - 1] == num[i - 2]:
                res.append(num[i] * 3)
        return str(max(res or ['']))
