#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: The Time When the Network Becomes Idle.py 
@time: 2021/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        def dijkstra2(successors, s):
            S = []
            S.append(s)
            n = len(successors)
            L = dict()
            L[s] = 0
            P = dict()
            P[s] = '-'

            # Iterate through the V/{s}-nodes and set L[j] to infinity and P[j] to s.
            for o in range(0, n):
                if o != s:
                    L[o] = float('inf')
                    P[o] = s

            # Visited vector.
            visited = [False] * n

            # Heapq
            queue = [(0, s)]

            while queue:
                par_len, v = heapq.heappop(queue)
                # v is unvisited
                if visited[v] is False:
                    visited[v] = True
                    for w, edge_len in successors[v].items():
                        # Check if the child is unvisited and compute the distance.
                        if visited[w] is False and edge_len + par_len < L[w]:
                            heapq.heappush(queue, (edge_len + par_len, w))
                            L[w] = edge_len + par_len
                            P[w] = v

            return L, P

        n = len(patience)
        dists = collections.defaultdict(dict)
        for e1, e2 in edges:
            dists[e1][e2] = 1
            dists[e2][e1] = 1
        L, P = dijkstra2(dists, 0)

        ret = 0
        for i, p in enumerate(patience):
            if i > 0:
                if (2 * L[i]) % patience[i] == 0:
                    res = 4 * L[i] - patience[i]
                else:
                    res = 4 * L[i] - (2 * L[i] % patience[i])
                ret = max(ret, res)
        return ret + 1


so = Solution()
print(so.networkBecomesIdle(edges=[[0, 1], [1, 2]], patience=[0, 2, 1]))
print(so.networkBecomesIdle(edges=[[0, 1], [0, 2], [1, 2]], patience=[0, 10, 10]))
