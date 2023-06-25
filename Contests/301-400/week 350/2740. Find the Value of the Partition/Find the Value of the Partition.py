"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Value of the Partition.py
@time: 20230619
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ret = float('inf')
        for i in range(len(nums) - 1):
            ret = min(ret, abs(nums[i + 1] - nums[i]))
        return ret


so = Solution()
print(so.findValueOfPartition(nums=[1, 3, 2, 4]))
print(so.findValueOfPartition(nums=[100, 1, 10]))
