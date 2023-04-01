"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Shortest Cycle in a Graph.py
@time: 20230401
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans = float('inf')
        for start in range(n):
            queue = [(start, 0)]
            visited = [-1] * n
            visited[start] = 0
            while queue:
                node, dist = queue.pop(0)
                for nei in adj[node]:
                    if visited[nei] == -1:
                        queue.append((nei, dist + 1))
                        visited[nei] = dist + 1
                    elif nei != start and visited[nei] >= visited[node]:
                        ans = min(ans, visited[node] + visited[nei] + 1)
        if ans == float('inf'):
            return -1
        return ans
