"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Left and Right Sum Differences.py
@time: 20230627
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        for i, n in enumerate(nums[:-1]):
            left_sum.append(left_sum[-1] + n)
        right_sum = [0]
        for i, n in enumerate(nums[:0:-1]):
            right_sum.insert(0, right_sum[0] + n)
        ret = []
        for l, r in zip(left_sum, right_sum):
            ret.append(abs(l - r))
        return ret


so = Solution()
print(so.leftRightDifference(nums=[10, 4, 8, 3]))
