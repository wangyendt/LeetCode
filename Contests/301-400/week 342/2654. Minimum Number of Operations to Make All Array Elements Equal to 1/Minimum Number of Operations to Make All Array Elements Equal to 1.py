"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Number of Operations to Make All Array Elements Equal to 1.py
@time: 20230425
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
import math
from typing import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = sum(1 for num in nums if num == 1)
        if c != 0: return n - c
        ret = 1e10
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    ret = min(ret, j - i + (n - 1))
                    break
        return ret if ret != 1e10 else -1
