"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Collecting Chocolates.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [x * k for k in range(n)]
        for i in range(n):
            cur = nums[i]
            for k in range(n):
                cur = min(cur, nums[i - k])
                res[k] += cur
        return min(res)


so = Solution()
print(so.minCost(nums=[20, 1, 15], x=5))
print(so.minCost(nums=[15, 150, 56, 69, 214, 203], x=42))
