"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Design Graph With Shortest Path Calculator.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections
import heapq
from typing import *


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjacency_list = collections.defaultdict(list)

        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, edge_cost = edge
        self.adjacency_list[from_node].append((to_node, edge_cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]  # (cost, node)
        visited = set()

        while pq:
            cost, node = heapq.heappop(pq)

            if node == node2:
                return cost

            if node not in visited:
                visited.add(node)
                for neighbor, edge_cost in self.adjacency_list[node]:
                    if neighbor not in visited:
                        heapq.heappush(pq, (cost + edge_cost, neighbor))

        return -1
