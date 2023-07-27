"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Sum of Imbalance Numbers of All Subarrays.py
@time: 20230727
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i, x in enumerate(nums):
            vis = [False] * (n + 2)
            vis[x] = True
            cnt = 0
            for j in range(i + 1, n):
                x = nums[j]
                if not vis[x]:
                    cnt += 1 - vis[x - 1] - vis[x + 1]
                    vis[x] = True
                ans += cnt
        return ans
