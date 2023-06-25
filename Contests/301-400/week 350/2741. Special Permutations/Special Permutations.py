"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Special Permutations.py
@time: 20230620
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import functools
from typing import *


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n, MOD = len(nums), 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(prev, mask):
            if mask == (1 << n) - 1: return 1
            count = 0
            for i in range(n):
                if not (mask & (1 << i)) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    count += dfs(nums[i], mask | (1 << i))
            return count % MOD

        return dfs(1, 0)
