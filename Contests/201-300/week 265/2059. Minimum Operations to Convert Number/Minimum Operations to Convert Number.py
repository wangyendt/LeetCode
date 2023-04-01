#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Convert Number.py 
@time: 2021/10/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        nums = [n for n in nums if n != 0]
        res = collections.defaultdict(int)
        res[start] = 0
        stack = []
        seen = {start}
        for n in nums:
            for x in (start + n, start - n, start ^ n):
                if goal == x: return 1
                if 0 <= x <= 1000:
                    heapq.heappush(stack, (1, x))
                seen.add(x)
        while stack:
            # print(stack)
            v, k = heapq.heappop(stack)
            for n in nums:
                for x in (k + n, k - n, k ^ n):
                    if x in seen: continue
                    if x == goal: return v + 1
                    seen.add(x)
                    if 0 <= x <= 1000:
                        heapq.heappush(stack, (v + 1, x))
        return -1


so = Solution()
print(so.minimumOperations(nums=[1, 3], start=6, goal=4))
print(so.minimumOperations(nums=[3, 5, 7], start=0, goal=-4))
print(so.minimumOperations(nums=[2, 8, 16], start=0, goal=1))
print(so.minimumOperations(
    [-574938140, 347713845, 925500837, -396559946, -39213216, -696511059, -701862040, -547815957, -613314611, 814380075,
     446824702, 397447568, 709912715, 144793599, 812441247, -59489753, 857299470, 360355629, 85411951, -439873837,
     -477453514, -887964831, -914549223, 633449658, 452658511, 657134722, 1],
    827,
    -547815957))
