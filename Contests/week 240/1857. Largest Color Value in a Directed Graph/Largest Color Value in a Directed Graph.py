#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Color Value in a Directed Graph.py 
@time: 2021/05/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, dq, seen = len(colors), collections.deque(), set()
        nxt = [set() for _ in range(n)]
        pre = [0 for _ in range(n)]
        dicts = [{x: 1} for x in colors]

        for i, j in edges:
            if i == j:
                return -1
            nxt[i].add(j)
            pre[j] += 1

        for i in range(n):
            if not pre[i]:
                dq.append(i)
                seen.add(i)

        while dq:
            cur = dq.popleft()
            for cand in nxt[cur]:
                tmp = {colors[cand]: 1}
                for i, x in dicts[cur].items():
                    if i not in tmp:
                        tmp[i] = x
                    else:
                        tmp[i] += x
                for i, x in tmp.items():
                    if i not in dicts[cand]:
                        dicts[cand][i] = x
                    else:
                        dicts[cand][i] = max(dicts[cand][i], x)
                pre[cand] -= 1
                if not pre[cand] and cand not in seen:
                    seen.add(cand)
                    dq.append(cand)

        if len(seen) != n:
            return -1

        return max(max(i.values()) for i in dicts)
