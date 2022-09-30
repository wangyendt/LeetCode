"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find All Good Indices.py
@time: 20220930
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        pre = 1e7
        cnt = 0
        left = set()
        for i, n in enumerate(nums):
            if i >= N - k: break
            if cnt >= k:
                left.add(i)
            if n <= pre:
                cnt += 1
            else:
                cnt = 1
            pre = n
        pre = 1e7
        cnt = 0
        right = set()
        for i, n in enumerate(nums[::-1]):
            if N - 1 - i < k: break
            if cnt >= k:
                right.add(N - 1 - i)
            if n <= pre:
                cnt += 1
            else:
                cnt = 1
            pre = n
        # print(left, right)
        return sorted(left & right)


so = Solution()
print(so.goodIndices([2, 1, 3, 1, 2], 2))
print(so.goodIndices([478184, 863008, 716977, 921182, 182844, 350527, 541165, 881224], 1))
