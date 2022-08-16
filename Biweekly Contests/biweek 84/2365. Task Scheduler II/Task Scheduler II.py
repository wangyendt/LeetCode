#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Task Scheduler II.py 
@time: 2022/08/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        res = collections.defaultdict(int)
        day = collections.defaultdict(int)
        day[0] = 1
        res[tasks[0]] = 0
        for i, t in enumerate(tasks):
            if i == 0: continue
            if t not in res:
                res[t] = i
                day[i] = day[i - 1] + 1
                continue
            if day[i - 1] - space >= day[res[t]]:
                day[i] = day[i - 1] + 1
            else:
                day[i] = day[res[t]] + space + 1
            res[t] = i
        return day[len(tasks) - 1]


so = Solution()
print(so.taskSchedulerII(tasks=[1, 2, 1, 2, 3, 1], space=3))
print(so.taskSchedulerII(tasks=[5, 8, 8, 5], space=2))
