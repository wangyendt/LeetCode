#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Shifting Letters II.py 
@time: 2022/10/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import numpy as np


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = np.zeros((len(s),))
        for shift in shifts:
            start, end, sign = shift
            if sign == 0:
                arr[start:end + 1] -= 1
            else:
                arr[start:end + 1] += 1
        letters = 'abcdefghijklmnopqrstuvwxyz'
        s_int = np.array(list(map(lambda x: {k: float(i) for i, k in enumerate(letters)}[x], s)))
        s_int += arr
        s_int = s_int % 26
        s_int = s_int.astype(int)
        # print(s_int.tolist())
        # print(map(lambda x: letters[x], s_int.tolist()))
        return ''.join(map(lambda x: letters[x], s_int.tolist()))


so = Solution()
print(so.shiftingLetters(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
