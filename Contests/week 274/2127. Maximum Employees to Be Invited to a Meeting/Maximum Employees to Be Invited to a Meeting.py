#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Employees to Be Invited to a Meeting.py 
@time: 2022/01/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # if a likes b, construct an edge reversely (b -> a) to make following BFS easier
        invG = collections.defaultdict(set)
        for idx, fav in enumerate(favorite):
            invG[fav].add(idx)

        # Find all cycles
        N = len(favorite)
        cycles = []  # (start of cycle, length of cycle)
        for i in range(N):
            if favorite[i] != -1:  # not explored before, do a DFS here
                dist = {i: 0}  # record the order of exploration
                while favorite[i] != -1:
                    nxt = favorite[i]
                    favorite[i] = -1
                    if nxt in dist:  # detect cycle
                        cycles.append((nxt, len(dist) - dist[nxt]))  # the real cycle length
                        break
                    else:
                        i = nxt
                        dist[nxt] = len(dist)

        # Find extension path of 2-cycle
        def bfs(start, seen):
            q = collections.deque([(start, 0)])
            ans = 0
            while q:
                pos, dist = q.popleft()
                for neib in invG[pos]:
                    if neib in seen:
                        continue
                    seen.add(neib)
                    q.append((neib, dist + 1))
                    ans = max(ans, dist + 1)
            return ans

        max_cycle, cycle_2s = 0, 0
        for start, cycle_len in cycles:
            if cycle_len > 2:
                max_cycle = max(max_cycle, cycle_len)
            else:
                u, v = start, [neib for neib in invG[start] if start in invG[neib]][0]
                cycle_2s += 2 + bfs(u, {u, v}) + bfs(v, {u, v})
        return max(max_cycle, cycle_2s)
