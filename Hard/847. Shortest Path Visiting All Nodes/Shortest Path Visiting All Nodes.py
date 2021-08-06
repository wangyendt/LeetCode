#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Shortest Path Visiting All Nodes.py 
@time: 2021/08/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        seen = set()
        stack = collections.deque()
        for i, g in enumerate(graph):
            stack.append((i, 1 << i, 0))
        while stack:
            item, state, res = stack.popleft()
            # print(stack, state)
            if state == (1 << n) - 1: return res
            for g in graph[item]:
                if (g, state | 1 << g) not in seen:
                    seen.add((g, state | 1 << g))
                    stack.append((g, state | 1 << g, res + 1))


so = Solution()
print(so.shortestPathLength(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
