"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Maximum Sum With Exactly K Elements.py
@time: 20230505
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (max(nums) * 2 + k - 1) * k // 2
