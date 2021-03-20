#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize Score After N Operations.py 
@time: 2021/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools
import functools
import collections
import math


class Solution:
    def maxScore(self, nums):
        n = len(nums)
        gcds = {(j, k): math.gcd(nums[j], nums[k]) for j, k in itertools.combinations(range(n), 2)}

        @functools.lru_cache(None)
        def dfs(bitmask):
            if bitmask == 0: return 0

            cand = 0
            n_z_bits = [j for j in range(n) if bitmask & (1 << j)]
            for j, k in itertools.combinations(n_z_bits, 2):
                q = bitmask ^ (1 << j) ^ (1 << k)
                cand = max(cand, dfs(q) + (n + 2 - len(n_z_bits)) // 2 * gcds[j, k])
            return cand

        return dfs((1 << n) - 1)

    def maxScore2(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(range(n))
        res = dict()

        def gcd(v1, v2):
            if (v1, v2) not in res:
                res[(v1, v2)] = res[(v2, v1)] = math.gcd(v1, v2)
            return res[(v1, v2)]

        ret = 0
        for a in itertools.combinations(range(n), n // 2):
            b = s - set(a)
            for c in itertools.permutations(b):
                tmp1 = itertools.permutations(range(1, n // 2 + 1))
                tmp2 = list(zip(a, c))
                for t1 in tmp1:
                    t_res = sum(t1[j] * gcd(nums[tmp2[j][0]], nums[tmp2[j][1]]) for j in range(n // 2))
                    ret = max(ret, t_res)
        return ret


so = Solution()
# print(so.maxScore(nums=[3, 4, 6, 8]))
print(so.maxScore([171651, 546244, 880754, 412358]))
print(so.maxScore([327161, 405335, 360021, 441366, 834880, 197174, 270974, 114045, 265771, 943529]))
