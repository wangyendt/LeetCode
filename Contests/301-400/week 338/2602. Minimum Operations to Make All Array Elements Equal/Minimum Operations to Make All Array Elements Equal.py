"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Operations to Make All Array Elements Equal.py
@time: 20230512
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import bisect
import itertools
from typing import *


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] + list(itertools.accumulate(nums))
        for x in queries:
            i = bisect.bisect_left(nums, x)
            yield x * (2 * i - len(nums)) + prefix[-1] - 2 * prefix[i]
