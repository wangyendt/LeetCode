"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Score of a Path Between Two Cities.py
@time: 20221204
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        min_vals = {}
        for r1, r2, d in roads:
            g[r1].append([r2, d])
            g[r2].append([r1, d])

            if r1 not in min_vals:
                min_vals[r1] = d
            else:
                min_vals[r1] = min(min_vals[r1], d)

            if r2 not in min_vals:
                min_vals[r2] = d
            else:
                min_vals[r2] = min(min_vals[r2], d)

        seen = set()
        q = collections.deque([1])
        while q:
            v = q.popleft()
            for j in g[v]:
                if j[0] not in seen:
                    seen.add(j[0])
                    q.append(j[0])

        ret = float('inf')
        for i in seen:
            ret = min(ret, min_vals[i])
        return ret


so = Solution()
print(so.minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(so.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
