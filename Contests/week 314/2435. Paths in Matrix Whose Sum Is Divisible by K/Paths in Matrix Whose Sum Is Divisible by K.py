"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Paths in Matrix Whose Sum Is Divisible by K.py
@time: 20221009
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        mod = 10 ** 9 + 7
        for i, j in itertools.product(range(m), range(n)):
            if i == 0 and j == 0:
                dp[i][j][grid[i][j] % k] += 1
            elif i == 0:
                for key in range(k):
                    dp[i][j][(key + grid[i][j]) % k] += dp[i][j - 1][key] % mod
            elif j == 0:
                for key in range(k):
                    dp[i][j][(key + grid[i][j]) % k] += dp[i - 1][j][key] % mod
            else:
                for key in range(k):
                    dp[i][j][(key + grid[i][j]) % k] += dp[i][j - 1][key] % mod
                    dp[i][j][(key + grid[i][j]) % k] += dp[i - 1][j][key] % mod
        return dp[-1][-1][0]
