#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Distinct Roll Sequences.py 
@time: 2022/06/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6
        res = collections.defaultdict(int)
        mod = 10 ** 9 + 7
        p_next = {
            1: [2, 3, 4, 5, 6],
            2: [1, 3, 5],
            3: [1, 2, 4, 5],
            4: [1, 3, 5],
            5: [1, 2, 3, 4, 6],
            6: [1, 5]
        }
        for i in range(6):
            for j in p_next[i + 1]:
                res[(j, i + 1)] = 1
        for i in range(2, n):
            m = collections.defaultdict(int)
            for j in range(6):
                for k in p_next[j + 1]:
                    cur = 0
                    for l in p_next[k]:
                        if j + 1 != l:
                            cur += res[(l, k)] % mod
                    m[(k, j + 1)] = cur
            res = m
        return sum(v for k, v in res.items()) % mod


so = Solution()
print(so.distinctSequences(1))
