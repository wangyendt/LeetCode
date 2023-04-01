#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum AND Sum of Array.py 
@time: 2022/02/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        res = collections.defaultdict(list)
        for i in range(1, 16):
            res1 = []
            for j in range(1, numSlots + 1):
                res2 = i & j
                res1.append((res2, j))
            res1.sort(key=lambda x: (-x[0], x[1]))
            res[i] = res1.copy()
        # print(res)
        ret = 0
        import random
        k1 = 0
        while k1 < 300:
            k1 += 1
            ret1 = 0
            res3 = collections.defaultdict(int)
            random.shuffle(nums)
            for n in nums:
                for k, v in res[n]:
                    if res3[v] == 2:
                        continue
                    else:
                        ret1 += k
                        res3[v] += 1
                        break
            ret = max(ret, ret1)
        return ret


so = Solution()
print(so.maximumANDSum(nums=[1, 2, 3, 4, 5, 6], numSlots=3))
print(so.maximumANDSum([14, 7, 9, 8, 2, 4, 11, 1, 9], 8))
