"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Destroy Sequential Targets.py
@time: 20221030
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        res = []
        for n in nums:
            res.append(n % space)
        cnter = collections.Counter(res)
        key = cnter.most_common()[0][0]
        for i, r in enumerate(res):
            if r == key:
                return nums[i]


so = Solution()
print(so.destroyTargets(nums=[3, 7, 8, 1, 1, 5], space=2))
