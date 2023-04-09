#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Reverse Operations.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
from sortedcontainers import SortedList


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        remaining = [SortedList(), SortedList()]
        banned = set(banned)
        for u in range(n):
            if u != p and u not in banned:
                remaining[u & 1].add(u)

        queue = [p]
        dist = [-1] * n
        dist[p] = 0
        for node in queue:
            lo = max(node - k + 1, 0)
            lo = 2 * lo + k - 1 - node
            hi = min(node + k - 1, n - 1) - (k - 1)
            hi = 2 * hi + k - 1 - node

            for nei in list(remaining[lo % 2].irange(lo, hi)):
                queue.append(nei)
                dist[nei] = dist[node] + 1
                remaining[lo % 2].remove(nei)

        return dist
