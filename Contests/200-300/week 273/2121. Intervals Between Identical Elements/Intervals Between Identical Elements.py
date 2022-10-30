#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Intervals Between Identical Elements.py 
@time: 2021/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        cnter = collections.defaultdict(list)
        for i, a in enumerate(arr):
            cnter[a].append(i)
        ret = [0] * len(arr)
        for k, v in cnter.items():
            if len(v) == 1:
                ret[v[0]] = 0
                continue
            res1 = [0]
            res2 = [0]
            for i in range(len(v) - 1):
                if i == 0:
                    res1.append(v[i + 1] - v[i])
                    res2.append(v[~i] - v[~(i + 1)])
                else:
                    res1.append(res1[-1] + (v[i + 1] - v[i]) * (i + 1))
                    res2.append(res2[-1] + (v[~i] - v[~(i + 1)]) * (i + 1))
            # print(res1)
            # print(res2)
            for i in range(len(v)):
                ret[v[i]] = res1[i] + res2[~i]
        return ret


so = Solution()
print(so.getDistances([1, 1, 1, 1, 1]))
