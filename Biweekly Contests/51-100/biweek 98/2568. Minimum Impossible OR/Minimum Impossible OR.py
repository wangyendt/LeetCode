"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Impossible OR.py
@time: 20230330
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(1000):
            if (1 << i) not in nums_set:
                return 1 << i


so = Solution()
print(so.minImpossibleOR(nums=[4, 32, 16, 8, 8, 75, 1, 2]))
