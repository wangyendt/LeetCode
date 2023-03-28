"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Array Concatenation Value.py
@time: 20230223
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ret = 0
        while nums:
            if len(nums) == 1:
                ret += nums.pop()
            else:
                a, b = nums.pop(0), nums.pop()
                ret += b
                while b:
                    a *= 10
                    b //= 10
                ret += a
        return ret
