#!/usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:  wangye
@file: Two Sum Less Than K.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import sys


class Solution:
    def twoSumLessThanK(self, A: list, K: int) -> int:
        A.sort()
        ret = -sys.maxsize
        b = False
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K:
                    ret = max(ret, A[i] + A[j])
                    b = True
                else:
                    break
        return ret if not b else -1
