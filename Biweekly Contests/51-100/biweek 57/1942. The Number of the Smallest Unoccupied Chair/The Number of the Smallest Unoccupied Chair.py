#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: The Number of the Smallest Unoccupied Chair.py 
@time: 2021/07/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect
import collections
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        idle = list(range(n))
        heapq.heapify(idle)
        leave = collections.deque()
        leave_key = collections.deque()
        sitten = dict()
        for i, t in sorted(enumerate(times), key=lambda x: x[1][1]):
            leave.append((t[1], i))
            leave_key.append(t[1])
        for i, t in sorted(enumerate(times), key=lambda x: x[1][0]):
            idx = bisect.bisect_right(leave_key, t[0])
            for _ in range(idx):
                heapq.heappush(idle, sitten[leave[0][1]])
                leave.popleft()
                leave_key.popleft()
            ret = heapq.heappop(idle)
            sitten[i] = ret
            if i == targetFriend:
                return ret


so = Solution()
print(so.smallestChair(times=[[3, 10], [1, 5], [2, 6]], targetFriend=0))
print(so.smallestChair(
    [[33889, 98676], [80071, 89737], [44118, 52565], [52992, 84310], [78492, 88209], [21695, 67063], [84622, 95452],
     [98048, 98856], [98411, 99433], [55333, 56548], [65375, 88566], [55011, 62821], [48548, 48656], [87396, 94825],
     [55273, 81868], [75629, 91467]], 6))
tmp = []
import random

for i in range(10000):
    rnd = random.randint(i * 2 + 2, 100000)
    if rnd == i * 2 + 1:
        rnd += 1
    tmp.append([i * 2 + 1, rnd])
random.shuffle(tmp)
print(so.smallestChair(tmp, 2656))
