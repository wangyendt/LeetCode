"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Modify Graph Edge Weights.py
@time: 20230524
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import heapq
from typing import *
import collections


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        inf = float('inf')
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])

        def dijkstra(source, adj, skip_negative):
            pq = [[0, source]]
            dist = collections.defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heapq.heappush(pq, [d2, nei])

            return dist, parent

        distR, parentR = dijkstra(destination, adj, skip_negative=True)
        if distR.get(source, inf) < target:
            return []
        dist, parent = dijkstra(source, adj, skip_negative=False)
        if dist[destination] > target:
            return []

        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path = path[::-1]

        edges = {(min(u, v), max(u, v)): w for u, v, w in edges}

        walked = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            e = (min(u, v), max(u, v))
            if edges[e] == -1:
                edges[e] = max(target - distR.get(v, inf) - walked, 1)
            walked += edges[e]

        for e, w in edges.items():
            if w == -1:
                edges[e] = 2 * (10 ** 9)

        return [[u, v, w] for (u, v), w in edges.items()]
