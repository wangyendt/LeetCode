#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Subtrees With Max Distance Between Cities
@time: 2020/10/11 12:06
"""

from typing import *


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(edges, start, i):  # returns whether or not we are a tree
            seen = set()
            stack = [start]
            while len(stack) > 0:
                curr = stack.pop()
                if curr not in seen:
                    seen.add(curr)
                    for neigh in edges[curr]:
                        stack.append(neigh)
            nodeSet = set()
            for j in range(n):
                if i & (1 << j):
                    nodeSet.add(j)
            return nodeSet == seen

        def diameter(edges, start):  # returns the diameter of tree
            farthest = start
            farthestDist = 0
            seen = set()
            stack = [(start, 0)]
            while len(stack) > 0:
                curr, dist = stack.pop()
                if curr not in seen:
                    seen.add(curr)
                    if dist > farthestDist:
                        farthest = curr
                        farthestDist = dist
                    for neigh in edges[curr]:
                        stack.append((neigh, dist + 1))
            start = farthest
            farthestDist = 0
            seen = set()
            stack = [(start, 0)]
            while len(stack) > 0:
                curr, dist = stack.pop()
                if curr not in seen:
                    seen.add(curr)
                    if dist > farthestDist:
                        farthest = curr
                        farthestDist = dist
                    for neigh in edges[curr]:
                        stack.append((neigh, dist + 1))
            return farthestDist

        diameterCounts = defaultdict(int)
        for i in range(1, 2 ** n):
            if sum([int(elem) for elem in bin(i)[2:]]) == 1:
                continue
            subTreeEdges = defaultdict(list)
            for edge in edges:
                l, m = edge
                l -= 1
                m -= 1
                if i & (1 << l) and i & (1 << m):
                    subTreeEdges[l].append(m)
                    subTreeEdges[m].append(l)
            start = None
            for j in range(n):
                if i & (1 << j):
                    start = j
                    break
            isSubtree = dfs(subTreeEdges, start, i)
            if isSubtree:
                diameterCounts[diameter(subTreeEdges, start)] += 1
            else:
                pass

        return [diameterCounts[i] for i in range(1, n)]
