#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Connecting Cities With Minimum Cost.py 
@time: 2019/07/27
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minimumCost(self, n: int, c: list(list())) -> int:
        def find(x):
            if x != up[x]:
                up[x] = find(up[x])
            return up[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                up[a] = b
                cnt[b] += cnt[a]
                return True
            return False

        up = [i for i in range(n + 1)]
        cnt = [1] * (n + 1)
        c.sort(key=lambda x: x[2])
        ret = 0
        for u, v, w in c:
            if union(u, v):
                ret += w
        return ret if max(cnt) == n else -1


so = Solution()
print(so.minimumCost(5, [[2, 1, 3267], [3, 2, 25910], [4, 1, 30518]]))
print(so.minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
print(so.minimumCost(4, [[1, 2, 3], [3, 4, 4]]))
print(so.minimumCost(5, [[2, 1, 50459], [3, 2, 47477], [4, 2, 52585], [5, 3, 16477]]))
