#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Restricted Paths From First to Last Node.py 
@time: 2021/03/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import functools
import heapq


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))
        minHeap = [(0, n)]  # dist, node
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        while minHeap:
            d, u = heapq.heappop(minHeap)
            if d != dist[u]: continue
            for w, nei in graph[u]:
                if dist[nei] > dist[u] + w:
                    dist[nei] = dist[u] + w
                    heapq.heappush(minHeap, (dist[nei], nei))

        @functools.lru_cache(None)
        def dfs(src):
            if src == n: return 1  # Find a path to reach to destination
            ans = 0
            for _, nei in graph[src]:
                if dist[src] > dist[nei]:
                    ans += dfs(nei)
            return ans

        ans = dfs(1)
        return ans % (10 ** 9 + 7)


so = Solution()
print(so.countRestrictedPaths(
    n=5,
    edges=[[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]])
)
