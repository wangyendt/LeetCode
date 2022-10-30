#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Parallel Courses.py 
@time: 2019/07/28
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minimumSemesters(self, n: int, r: List[List[int]]) -> int:
        post = [[] for i in range(n + 1)]
        pre = [set() for i in range(n + 1)]
        cand = set(range(1, n + 1))
        for u, v in r:
            post[u].append(v)
            pre[v].add(u)
            cand.discard(v)
        s = 0
        taken = set()
        while cand:
            s += 1
            nc = set()
            taken |= cand
            for i in cand.copy():
                for j in post[i]:
                    pre[j].discard(i)
                    if not pre[j]:
                        nc.add(j)
            cand = nc
        return s if len(taken) == n else -1
