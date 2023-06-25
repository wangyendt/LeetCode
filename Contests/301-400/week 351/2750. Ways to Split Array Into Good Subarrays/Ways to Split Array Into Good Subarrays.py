"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Ways to Split Array Into Good Subarrays.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import math
from typing import *


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        while nums:
            if nums[0] == 0:
                nums.pop(0)
            else:
                break
        while nums:
            if nums[-1] == 0:
                nums.pop()
            else:
                break
        ones = []
        for i, n in enumerate(nums):
            if n == 1: ones.append(i)
        if not ones: return 0
        diffs = []
        # print(ones)
        for i, one in enumerate(ones[1:]):
            diffs.append(one - ones[i])
        # print(diffs)
        if not diffs: return 1
        res = 1
        for diff in diffs:
            res = (res * diff) % MOD
        return res


so = Solution()
print(so.numberOfGoodSubarraySplits(nums=[0, 1, 0, 0, 1]))
print(so.numberOfGoodSubarraySplits(nums=[0, 1, 0]))
