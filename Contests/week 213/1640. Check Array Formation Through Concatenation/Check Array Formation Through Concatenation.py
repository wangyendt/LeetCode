#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check Array Formation Through Concatenation.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if sorted(arr) != sorted(sum(pieces, [])):
            return False
        idx_dict = dict()
        res = []
        for a in arr:
            for i in range(len(pieces)):
                if a in pieces[i]:
                    idx_dict[a] = i
                    res.append(i)
                    break
        res2 = []
        last = -1
        for r in res:
            if r != last:
                res2.append(r)
            last = r
        res3 = [pieces[r] for r in res2]
        return arr == sum(res3, [])
