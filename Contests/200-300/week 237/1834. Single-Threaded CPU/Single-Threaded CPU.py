#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Single-Threaded CPU.py 
@time: 2021/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        h = []
        time = tasks[0][0]
        while len(res) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= time):
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if h:
                t_diff, original_index = heapq.heappop(h)
                time += t_diff
                res.append(original_index)
            elif i < len(tasks):
                time = tasks[i][0]
        return res


so = Solution()
# print(so.getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))
# print(so.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))
print(so.getOrder(
    [[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18],
     [46, 39], [12, 24]]))
