#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Second Minimum Time to Reach Destination.py
@time: 2021/10/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import math
import heapq


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        D = [[] for _ in range(n + 1)]
        D[1] = [0]
        G, heap = collections.defaultdict(list), [(0, 1)]

        for a, b in edges:
            G[a] += [b]
            G[b] += [a]

        while heap:
            min_dist, idx = heapq.heappop(heap)
            if idx == n and len(D[n]) == 2: return max(D[n])

            for neib in G[idx]:
                if (min_dist // change) % 2 == 0:
                    cand = min_dist + time
                else:
                    cand = math.ceil(min_dist / (2 * change)) * (2 * change) + time

                l = len(D[neib])

                if (l == 0) or (l == 1 and D[neib][0] != cand) or (
                        l == 2 and cand < max(D[neib]) and cand != min(D[neib])):
                    D[neib] += [cand]
                    heapq.heappush(heap, (cand, neib))

                if len(D[neib]) == 3:
                    D[neib].remove(max(D[neib]))


so = Solution()
print(so.secondMinimum(n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5))
print(so.secondMinimum(n=2, edges=[[1, 2]], time=3, change=2))
