#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Array With Elements Not Equal to Average of Neighbors.py 
@time: 2021/08/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq
import collections


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = []
        nums.sort()
        for i in range(n):
            if i & 1:
                ret.append(nums.pop())
            else:
                ret.append(nums.pop(0))
        return ret

        for k, v in cnter.items():
            heapq.heappush(res, (-v, k))
        print(f'{m=},{diffs=},{res=}')
        ans = []
        for i in range(n - 2):
            v1, k1 = heapq.heappop(res)
            if i == 0:
                ans.append(k1)
                v1 += 1
                heapq.heappush(res, (v1, k1))
                continue
            if k1 == ans[-1]:
                v2, k2 = heapq.heappop(res)
                ans.append(k2)
                v2 += 1
                heapq.heappush(res, (v2, k2))
            else:
                ans.append(k1)
            heapq.heappush(res, (v1, k1))
        v_, k_ = heapq.heappop(res)
        ans.append(k_)
        ans.sort()
        ans.append(0)
        for i, a in enumerate(ans):
            ans[i] += m
        return ans


so = Solution()
print(so.rearrangeArray(nums=[1, 1, 3, 4, 5]))
