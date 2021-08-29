#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Work Sessions to Finish the Tasks.py 
@time: 2021/08/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools
from functools import reduce

import math


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        self.ret = float('inf')
        nums = tasks
        size = len(nums)
        visited = [False] * len(nums)
        nums.sort()
        self.sums = sum(nums)

        def backtrack(tmp, rem, cnt):
            if tmp:
                if rem + tmp[-1] <= sessionTime:
                    rem += tmp[-1]
                else:
                    cnt += 1
                    rem = tmp[-1]
                if self.ret <= cnt + math.ceil(self.sums // sessionTime):
                    return
            if len(tmp) == size:
                self.ret = min(self.ret, cnt)
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    self.sums -= nums[i]
                    tmp.append(nums[i])
                    backtrack(tmp, rem, cnt)
                    tmp.pop()
                    visited[i] = False
                    self.sums+=nums[i]

        backtrack([], 0, 1)

        return self.ret


so = Solution()
print(so.minSessions(tasks=[1, 2, 3, 4, 2], sessionTime=15))
print(so.minSessions([2, 3, 3, 4, 4, 4, 6, 7, 8, 9, 10], 15))
print(so.minSessions([2, 3, 3, 4, 4, 4, 6, 7, 8, 9, 10, 8, 6, 4], 15))
print(so.minSessions([1, 2, 3], 3))
