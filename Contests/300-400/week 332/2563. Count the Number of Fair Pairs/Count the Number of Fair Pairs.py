"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count the Number of Fair Pairs.py
@time: 20230223
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ret = 0
        for i, n in enumerate(nums):
            idx1 = bisect.bisect_left(nums, lower - n)
            idx2 = bisect.bisect_right(nums, upper - n)
            ret += max(0, idx2 - idx1)
            if idx1 <= i < idx2:
                ret -= 1
        return ret // 2


so = Solution()
print(so.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6))
