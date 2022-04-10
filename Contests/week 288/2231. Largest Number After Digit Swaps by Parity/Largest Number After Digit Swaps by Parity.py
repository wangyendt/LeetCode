#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Number After Digit Swaps by Parity.py 
@time: 2022/04/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        num_list = list(str(num))
        even, odd = [], []
        even_indices = []
        for i, n in enumerate(num_list):
            if int(n) & 1:
                odd.append(n)
            else:
                even.append(n)
                even_indices.append(i)
        even.sort()
        odd.sort()
        p = 0
        res = []
        while even or odd:
            if p in even_indices:
                res.append(even.pop())
            else:
                res.append(odd.pop())
            p += 1
        return int(''.join(res))
