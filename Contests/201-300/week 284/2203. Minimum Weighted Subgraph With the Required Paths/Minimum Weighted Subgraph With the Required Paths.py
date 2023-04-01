#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Weighted Subgraph With the Required Paths.py 
@time: 2022/03/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        G1 = collections.defaultdict(list)
        G2 = collections.defaultdict(list)
        for a, b, w in edges:
            G1[a].append((b, w))
            G2[b].append((a, w))

        def Dijkstra(graph, K):
            q, t = [(0, K)], {}
            while q:
                time, node = heapq.heappop(q)
                if node not in t:
                    t[node] = time
                    for v, w in graph[node]:
                        heapq.heappush(q, (time + w, v))
            return [t.get(i, float("inf")) for i in range(n)]

        arr1 = Dijkstra(G1, src1)
        arr2 = Dijkstra(G1, src2)
        arr3 = Dijkstra(G2, dest)

        ans = float("inf")
        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])

        return ans if ans != float("inf") else -1
