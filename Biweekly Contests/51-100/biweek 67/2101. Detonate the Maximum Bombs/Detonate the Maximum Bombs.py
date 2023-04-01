#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Detonate the Maximum Bombs.py 
@time: 2021/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = collections.defaultdict(set)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if (bombs[j][0] - bombs[i][0]) ** 2 + (bombs[j][1] - bombs[i][1]) ** 2 <= bombs[i][2] ** 2:
                        res[i].add(j)
        cnter = collections.defaultdict(int)
        mems = collections.defaultdict(set)
        for i in range(n):
            stack = [i]
            seen = set()
            res_i = res.copy()
            while stack:
                s = stack.pop()
                if s in mems:
                    seen |= mems[s]
                    continue
                seen.add(s)
                for item in res_i[s]:
                    if item not in seen:
                        stack.append(item)
            mems[i] = seen
            cnter[i] = len(seen)
        return max(cnter.items(), key=lambda x: x[1])[1] or 1


so = Solution()
print(so.maximumDetonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
