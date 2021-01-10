#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize Hamming Distance After Swap Operations.py 
@time: 2021/01/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            px, py = map(find, (x, y))
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[px] = py
                    if rank[px] == rank[py]:
                        rank[py] += 1

        n = len(source)
        parent, rank = list(range(n)), [0] * n
        counters = collections.defaultdict(collections.Counter)
        for i, j in allowedSwaps:
            union(i, j)
        for i, (s, t) in enumerate(zip(source, target)):
            g = find(i)
            counters[g][s] += 1
            counters[g][t] -= 1
        return sum(val for counter in counters.values() for val in counter.values() if val > 0)


so = Solution()
print(so.minimumHammingDistance(source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]))
print(so.minimumHammingDistance(source=[5, 1, 2, 4, 3], target=[1, 5, 4, 2, 3],
                                allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]]))
