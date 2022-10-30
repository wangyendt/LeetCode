"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Longest Subarray With Maximum Bitwise AND.py
@time: 20220930
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        cnt = 0
        ret = 0
        for n in nums:
            if n == max_and:
                cnt += 1
            else:
                cnt = 0
            ret = max(ret, cnt)
        return ret
