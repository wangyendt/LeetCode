"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Painting the Walls.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [float('inf')] * n
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]
