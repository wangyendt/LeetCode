"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Relocate Marbles.py
@time: 20230804
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        res = collections.Counter(nums)
        for i, j in zip(moveFrom, moveTo):
            if i == j: continue
            res[j] += res[i]
            res[i] = 0
        return sorted([r for r in res.keys() if res[r] > 0])


so = Solution()
print(so.relocateMarbles(nums=[1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5]))
print(so.relocateMarbles([3, 4], [4, 3, 1, 2, 2, 3, 2, 4, 1], [3, 1, 2, 2, 3, 2, 4, 1, 1]))
