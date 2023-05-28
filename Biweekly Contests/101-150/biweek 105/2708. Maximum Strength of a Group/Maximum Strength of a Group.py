"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Maximum Strength of a Group.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import copy
from typing import *


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        prod = set()
        ret = -1e30
        if 0 in nums:
            ret = 0
            nums = [n for n in nums if n != 0]
        for n in nums:
            prod_ = copy.copy(prod)
            ret = max(ret, n)
            for p in prod:
                r = p * n
                ret = max(ret, r)
                prod_.add(r)
            prod_.add(n)
            prod = prod_
        return ret


so = Solution()
print(so.maxStrength(nums=[3, -1, -5, 2, 5, -9]))
print(so.maxStrength(nums=[0, 7]))
