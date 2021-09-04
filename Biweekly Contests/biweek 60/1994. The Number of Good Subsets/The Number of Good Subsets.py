#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: The Number of Good Subsets.py 
@time: 2021/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
from itertools import chain, combinations
import functools


class Solution:
    def numberOfGoodSubsets(self, nums):
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = Counter(nums)
        bm = [sum(1 << i for i, p in enumerate(P) if x % p == 0) for x in range(31)]
        bad = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
        M = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(mask, num):
            if num == 1: return 1
            ans = dp(mask, num - 1)
            if num not in bad and mask | bm[num] == mask:
                ans += dp(mask ^ bm[num], num - 1) * cnt[num]
            return ans % M

        return ((dp(1023, 30) - 1) * pow(2, cnt[1], M)) % M

    def numberOfGoodSubsets2(self, nums: List[int]) -> int:
        nums = [n for n in nums if n not in {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}]
        factors = {
            2: {2}, 3: {3}, 5: {5}, 6: {2, 3}, 7: {7}, 10: {2, 5}, 11: {11}, 13: {13},
            14: {2, 7}, 15: {3, 5}, 17: {17}, 19: {19}, 21: {3, 7}, 22: {2, 11}, 23: {23},
            26: {2, 13}, 29: {29}, 30: {2, 3, 5}
        }
        farewell = collections.defaultdict(set)
        keys = list(factors.keys())
        nn = len(factors.keys())
        for i in range(nn):
            for j in range(i + 1, nn):
                if len(factors[keys[i]] & factors[keys[j]]) >= 1:
                    farewell[keys[i]].add(keys[j])
                    farewell[keys[j]].add(keys[i])
        # print(farewell)
        cnt = collections.Counter(nums)
        s = set(cnt.keys()) - {1}
        ret = 0
        MOD = 10 ** 9 + 7
        gain = (2 ** cnt[1]) if 1 in cnt else 1

        @functools.lru_cache(None)
        def get_prod(arr):
            if len(arr) == 1: return cnt[arr[0]]
            return functools.reduce(
                lambda x, y: x * y,
                [cnt[a] for a in arr]
            )

        mems = set()
        for item in chain.from_iterable(combinations(s, t) for t in range(len(s) + 1)):
            if len(item) == 1 and item[0] == 1: continue
            ss = set(item)
            if not ss: continue
            tt = tuple(sorted(ss))
            if tt in mems: continue
            for sss in ss:
                if any(ssss in farewell[sss] for ssss in ss):
                    mems.add(tt)
                    break
            else:
                ret = (ret + (get_prod(tt))) % MOD
        return (ret * gain) % MOD


so = Solution()
print(so.numberOfGoodSubsets([1, 1, 1, 2, 2, 3, 4, 30]))
print(so.numberOfGoodSubsets(nums=[4, 2, 3, 15]))
print(so.numberOfGoodSubsets(list(range(1, 31)) * 100))
print(so.numberOfGoodSubsets([18, 28, 2, 17, 29, 30, 15, 9, 12]))
print(so.numberOfGoodSubsets([6, 8, 1, 8, 6, 5, 6, 11, 17]))
print(so.numberOfGoodSubsets(
    [5, 10, 1, 26, 24, 21, 24, 23, 11, 12, 27, 4, 17, 16, 2, 6, 1, 1, 6, 8, 13, 30, 24, 20, 2, 19]))
