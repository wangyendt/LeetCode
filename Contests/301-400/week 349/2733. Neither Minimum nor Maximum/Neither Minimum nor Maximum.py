"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Neither Minimum nor Maximum.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        m, M = min(nums), max(nums)
        for n in nums:
            if n != m and n != M:
                return n
        return -1
