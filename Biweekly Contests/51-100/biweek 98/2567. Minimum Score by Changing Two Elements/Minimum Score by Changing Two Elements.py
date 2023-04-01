"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Score by Changing Two Elements.py
@time: 20230330
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],
            nums[-2] - nums[1],
            nums[-3] - nums[0]
        )
