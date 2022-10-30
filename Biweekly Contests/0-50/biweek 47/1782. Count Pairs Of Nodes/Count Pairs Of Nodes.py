#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Pairs Of Nodes.py 
@time: 2021/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
import bisect
from typing import *


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        deg = [0] * n
        for x, y in edges:
            deg[x - 1] += 1
            deg[y - 1] += 1

        wtf = Counter()
        for x, y in edges:
            wtf[(min(x, y), max(x, y))] += 1

        # print(wtf)

        s = sorted(deg)

        ans = list()
        for q in queries:
            tot = 0
            for x in range(n):
                it = bisect.bisect_left(s, q - deg[x] + 1)
                tot += n - it
                if deg[x] + deg[x] > q:
                    tot -= 1
            # print(tot)
            for (x, y), z in wtf.items():
                if deg[x - 1] + deg[y - 1] > q >= deg[x - 1] + deg[y - 1] - z:
                    tot -= 2
            ans.append(tot // 2)

        return ans

    def countPairs2(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        aa = [a for (a, b) in edges]
        bb = [b for (a, b) in edges]
        c = collections.Counter(aa + bb)
        cc = collections.Counter([(a, b) for (a, b) in edges])

        ar = []
        for a in range(1, n):
            for b in range(a + 1, n + 1):
                ar.append(c[a] + c[b] - cc[(a, b)] - cc[(b, a)])
        ar.sort()

        res = []
        for q in queries:
            i = bisect.bisect_right(ar, q)
            res.append(len(ar) - i)
        return res
