#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Total Cost to Hire K Workers.py 
@time: 2022/11/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq
from sortedcontainers import SortedList


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if 2 * candidates >= len(costs):
            return sum(heapq.nsmallest(k, costs))
        left = SortedList(costs[:candidates])
        right = SortedList(costs[-candidates:])
        # print(len(costs))
        # print(left, right)
        cnt = 0
        n = len(costs)
        left_ptr = candidates - 1
        right_ptr = n - candidates
        ret = 0
        while cnt < k:
            if left_ptr >= right_ptr - 1:
                break
            if left[0] <= right[0]:
                ret += left[0]
                left.pop(0)
                left.add(costs[left_ptr + 1])
                left_ptr += 1
            else:
                ret += right[0]
                right.pop(0)
                right.add(costs[right_ptr - 1])
                right_ptr -= 1
            cnt += 1
        else:
            return ret
        return ret + sum(heapq.nsmallest(k - cnt, left + right))


so = Solution()
print(so.totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
print(so.totalCost(costs=[1, 2, 4, 1], k=3, candidates=3))
print(so.totalCost(costs=[1, 2, 4, 1], k=2, candidates=3))
print(so.totalCost(costs=[1, 2, 4, 1], k=3, candidates=2))
print(so.totalCost([28, 35, 21, 13, 21, 72, 35, 52, 74, 92, 25, 65, 77, 1, 73, 32, 43, 68, 8, 100, 84, 80, 14, 88, 42, 53, 98, 69, 64, 40, 60, 23, 99, 83, 5, 21, 76, 34], 32, 12))
print(so.totalCost([18, 64, 12, 21, 21, 78, 36, 58, 88, 58, 99, 26, 92, 91, 53, 10, 24, 25, 20, 92, 73, 63, 51, 65, 87, 6, 17, 32, 14, 42, 46, 65, 43, 9, 75], 13, 23))
