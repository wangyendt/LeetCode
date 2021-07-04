#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Ways to Build Rooms in an Ant Colony.py 
@time: 2021/06/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import math


class Solution:
    def waysToBuildRooms(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(arr):
            g[pre].append(cur)

        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * math.comb(l + r, r)) % MOD
                l += r
            return ans, l + 1

        return dfs(0)[0]
