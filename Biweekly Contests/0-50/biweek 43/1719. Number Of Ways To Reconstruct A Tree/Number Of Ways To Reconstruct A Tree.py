#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number Of Ways To Reconstruct A Tree.py 
@time: 2021/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        n = 0
        a = set()
        for x in pairs:
            n = max(n, x[0], x[1])
            a.add(x[0])
            a.add(x[1])
        d = [0] * (n + 1)
        e = [[] for _ in range(n + 1)]
        for x in pairs:
            d[x[0]] += 1
            d[x[1]] += 1
            e[x[0]].append(x[1])
            e[x[1]].append(x[0])

        roots = set()
        a = list(a)

        def work(a):
            if len(a) == 1:
                return 1
            c = 0
            o = -1
            for x in a:
                if d[x] == len(a) - 1 + len(roots):
                    c += 1
                    o = x
            if c == 0:
                return 0
            roots.add(o)
            f = set()
            aa = []
            for x in a:
                if x not in roots and x not in f:
                    q = [x]
                    f.add(x)
                    t = 0
                    while t < len(q):
                        y = q[t]
                        t += 1
                        for z in e[y]:
                            if z not in roots and z not in f:
                                q.append(z)
                                f.add(z)
                    aa.append(q)
            for b in aa:
                r = work(b)
                if r == 0:
                    return 0
                c = max(r, c)
            roots.remove(o)
            return c

        r = work(a)
        if r > 1:
            return 2
        return r
