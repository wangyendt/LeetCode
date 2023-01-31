"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count Increasing Quadruplets.py
@time: 20230131
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
from sortedcontainers import SortedList


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList([nums[0]])
        ans = 0
        for j in range(1, n):
            sl.add(nums[j])
            cnt = 1 if nums[j] < nums[-1] else 0
            for k in range(n - 2, j, -1):
                if nums[j] < nums[k]:
                    cnt += 1
                    continue
                ans += sl.bisect_left(nums[k]) * cnt
        return ans


so = Solution()
print(so.countQuadruplets(nums=[1, 3, 2, 4, 5]))
print(so.countQuadruplets(nums=[1, 2, 3, 4]))
print(so.countQuadruplets([2, 5, 3, 1, 4]))
