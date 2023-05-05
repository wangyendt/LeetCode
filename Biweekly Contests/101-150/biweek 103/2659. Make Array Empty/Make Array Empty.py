"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Make Array Empty.py
@time: 20230505
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {a: i for i, a in enumerate(nums)}
        res = n = len(nums)
        nums.sort()
        for i in range(1, n):
            if pos[nums[i]] < pos[nums[i - 1]]:
                res += n - i
        return res


so = Solution()
print(so.countOperationsToEmptyArray(nums=[3, 4, -1]))
