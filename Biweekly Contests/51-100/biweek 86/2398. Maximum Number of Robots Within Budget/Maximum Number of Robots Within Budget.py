#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Robots Within Budget.py 
@time: 2022/09/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        q = collections.deque()
        i, cur, ret = 0, 0, 0
        for j in range(n):
            while q and chargeTimes[j] >= chargeTimes[q[-1]]:
                q.pop()
            q.append(j)
            cur_max = chargeTimes[q[0]]
            cur += runningCosts[j]
            while cur * (j - i + 1) + cur_max > budget and i < j:
                cur -= runningCosts[i]
                if q and q[0] == i:
                    q.popleft()
                    cur_max = chargeTimes[q[0]]
                i += 1
            if i <= j and cur * (j - i + 1) + cur_max <= budget:
                ret = max(ret, j - i + 1)
        return ret


so = Solution()
print(so.maximumRobots(chargeTimes=[3, 6, 1, 3, 4], runningCosts=[2, 1, 3, 4, 5], budget=25))
print(so.maximumRobots(chargeTimes=[11, 12, 19], runningCosts=[10, 8, 7], budget=19))
