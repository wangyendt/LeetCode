"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Make Costs of Paths Equal in a Binary Tree.py
@time: 20230508
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = i * 2 + 1, i * 2 + 2
            res += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
        return res
