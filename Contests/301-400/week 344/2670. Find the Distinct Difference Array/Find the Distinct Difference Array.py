"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Distinct Difference Array.py
@time: 20230508
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]
