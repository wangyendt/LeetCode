#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Diet Plan Performance.py 
@time: 2019/09/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def dietPlanPerformance(self, calories: list, k: int, lower: int, upper: int) -> int:
        queue = collections.deque(maxlen=k)
        s, ret = 0, 0
        for cal in calories:
            queue.append(cal)
            s += cal
            if len(queue) < k:
                continue
            if s > upper:
                ret += 1
            elif s < lower:
                ret -= 1
            s -= queue.popleft()
        return ret


so = Solution()
print(so.dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3))
print(so.dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1))
print(so.dietPlanPerformance(calories=[6, 5, 0, 0], k=2, lower=1, upper=5))
print(so.dietPlanPerformance(calories=[], k=2, lower=1, upper=5))
print(so.dietPlanPerformance(calories=[6, 13, 8, 7, 10, 1, 12, 11], k=6, lower=5, upper=37))
