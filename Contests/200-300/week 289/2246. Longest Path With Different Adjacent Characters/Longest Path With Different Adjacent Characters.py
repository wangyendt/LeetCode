# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Longest Path With Different Adjacent Characters.py
@time: 2022/04/18
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import collections
import heapq
from typing import *


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        res = collections.defaultdict(list)
        for i, p in enumerate(parent):
            if p >= 0:
                res[p].append(i)

        ret = [0]

        def helper(i):
            candi = [0]
            for j in res[i]:
                cur = helper(j)
                if s[i] != s[j]:
                    candi.append(cur)

            candi = heapq.nlargest(2, candi)
            ret[0] = max(ret[0], sum(candi) + 1)
            return max(candi) + 1

        helper(0)
        return ret[0]


so = Solution()
print(so.longestPath(parent=[-1, 0, 0, 0], s="aabc"))
print(so.longestPath([-1, 0, 0, 1, 1, 2], "abacbe"))
print(so.longestPath([-1], "z"))
print(so.longestPath([-1, 0, 0], "aba"))
