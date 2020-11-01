#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Furthest Building You Can Reach.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        last = float('inf')
        # print(heights)
        for i, h in enumerate(heights):
            # print(i, h, last)
            if i > 0:
                if h > last:
                    if ladders > 0:
                        ladders -= 1
                        heapq.heappush(heap, h - last)
                    else:
                        if not heap:
                            if bricks >= h - last:
                                bricks -= h - last
                            else:
                                return i - 1
                        else:
                            # print(heap,h-last,heap[0],bricks)
                            # print(f'heap={heap},h-last={h - last},heap[0]={heap[0]},bricks={bricks}')
                            if h - last > heap[0]:
                                if bricks >= heap[0]:
                                    bricks -= heap[0]
                                    heapq.heappushpop(heap, h - last)
                                else:
                                    return i - 1
                            else:
                                if bricks >= h - last:
                                    bricks -= h - last
                                else:
                                    return i - 1
            last = h
        return len(heights) - 1


so = Solution()
print(so.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(so.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
print(so.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))
