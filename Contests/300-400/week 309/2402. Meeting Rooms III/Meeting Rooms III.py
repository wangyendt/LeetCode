#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Meeting Rooms III.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq
import collections


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count, free, taken = [0] * n, list(range(n)), []
        heapq.heapify(free)
        meetings.sort()
        prev = -1

        for start, end in meetings:
            # Reset start time.
            duration = end - start
            start = max(start, prev)
            end = start + duration

            # Free finished rooms
            while taken and taken[0][0] <= start:
                _, i = heapq.heappop(taken)
                heapq.heappush(free, i)

            # Delay current meeting if there is no free room.
            if not free:
                start = taken[0][0]
                end = start + duration
                # Free finished rooms
                while taken and taken[0][0] <= start:
                    _, i = heapq.heappop(taken)
                    heapq.heappush(free, i)

            # Assign a room
            i = heapq.heappop(free)
            count[i] += 1
            heapq.heappush(taken, [end, i])

            # Reset previous time
            prev = start

        return count.index(max(count))


so = Solution()
# print(so.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
# print(so.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(so.mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
print(so.mostBooked(3, [[39, 49], [28, 39], [9, 29], [10, 36], [22, 47], [2, 3], [4, 49], [46, 50], [45, 50], [17, 33]]))
