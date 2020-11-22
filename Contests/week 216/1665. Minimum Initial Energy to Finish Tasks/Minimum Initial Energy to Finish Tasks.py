#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Initial Energy to Finish Tasks
@time: 2020/11/22 11:15
"""

from typing import *


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[0] - x[1], x[0]))
        ret = 0
        for task in tasks[::-1]:
            ret += task[0] if ret >= task[1] else max(task[0], task[1] - ret)
        return ret


so = Solution()
print(so.minimumEffort(tasks=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
