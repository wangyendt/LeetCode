#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Score After Removals on a Tree.py 
@time: 2022/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n, m = len(nums), len(edges)
        G = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        xor_vals = nums[:]
        for e1, e2 in edges:
            G[e1].append(e2)
            G[e2].append(e1)
            degree[e1] += 1
            degree[e2] += 1
        xor = 0
        pq = collections.deque()
        seen = set()
        for i, num in enumerate(nums):
            xor ^= num
            if degree[i] == 1:
                pq.append(i)
                seen.add(i)
        res_children = collections.defaultdict(set)
        while pq:
            cur = pq.popleft()
            for neigh in G[cur]:
                if neigh not in seen:
                    res_children[neigh].add(cur)
                    res_children[neigh] |= res_children[cur]
                    xor_vals[neigh] ^= xor_vals[cur]
                degree[neigh] -= 1
                if degree[neigh] == 1 and len(seen) != n - 1:
                    pq.append(neigh)
                    seen.add(neigh)
        ret = 1e10
        for i in range(m - 1):
            for j in range(i + 1, m):
                p1, q1 = edges[i]
                p2, q2 = edges[j]

                if q1 in res_children[p1]: p1, q1 = q1, p1
                if q2 in res_children[p2]: p2, q2 = q2, p2

                if p2 in res_children[p1]:
                    group = [xor_vals[p2], xor_vals[p1] ^ xor_vals[p2], xor ^ xor_vals[p1]]
                elif p1 in res_children[p2]:
                    group = [xor_vals[p1], xor_vals[p2] ^ xor_vals[p1], xor ^ xor_vals[p2]]
                else:
                    group = [xor_vals[p1], xor_vals[p2], xor ^ xor_vals[p1] ^ xor_vals[p2]]
                ret = min(ret, max(group) - min(group))
        return ret
