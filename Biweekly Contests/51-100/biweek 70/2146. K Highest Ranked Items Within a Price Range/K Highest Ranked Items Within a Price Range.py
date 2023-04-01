#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: K Highest Ranked Items Within a Price Range.py 
@time: 2022/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        seen = set()
        r, c = start
        stack = [(-1, r, c)]
        # dis = collections.defaultdict(int)
        res = collections.defaultdict(tuple)
        m, n = len(grid), len(grid[0])
        while stack:
            sd, sr, sc = heapq.heappop(stack)  # stack.pop()
            if grid[sr][sc] == 0:
                continue
            if (sr, sc) not in seen:
                if pricing[0] <= grid[sr][sc] <= pricing[1]:
                    res[(sd + 1, grid[sr][sc], sr, sc)] = (sr, sc)
                # dis[(sr, sc)] = sd + 1
                seen.add((sr, sc))
                for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    nr, nc = sr + dr, sc + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        heapq.heappush(stack, (sd + 1, nr, nc))
                        # stack.append((nr, nc, sd + 1))
        # print(dis)
        # print(res)
        res2 = sorted(res.keys())
        # print(res2)
        ret = []
        for i in range(min(k,len(res2))):
            ret.append(list(res[res2[i]]))
        return ret


so = Solution()
print(so.highestRankedKItems(grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3))
print(so.highestRankedKItems(grid=[[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]], pricing=[2, 3], start=[2, 3], k=2))
print(so.highestRankedKItems(grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3))