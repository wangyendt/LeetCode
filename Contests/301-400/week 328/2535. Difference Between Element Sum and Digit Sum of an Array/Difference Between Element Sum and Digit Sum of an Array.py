"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Difference Between Element Sum and Digit Sum of an Array.py
@time: 20230115
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for n in nums:
            while n:
                s2 += (n % 10)
                n //= 10
        return abs(s1 - s2)
