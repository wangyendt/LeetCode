#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Jump Game III
@time: 2020/1/3 15:28
"""

import sys

sys.path.append('..')


class Solution:
    def canReach(self, arr: list, start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return (arr[start] == 0
                    or self.canReach(arr, start + arr[start])
                    or self.canReach(arr, start - arr[start]))
        return False

so = Solution()
print(so.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(so.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
print(so.canReach(arr=[3, 0, 2, 1, 2], start=2))
print(so.canReach(
    [31, 70, 40, 4, 27, 28, 44, 17, 8, 16,
     64, 14, 30, 17, 25, 61, 33, 50, 45, 67,
     12, 43, 72, 0, 26, 24, 33, 66, 22, 11,
     61, 15, 2, 18, 51, 37, 34, 7, 14, 29,
     37, 3, 40, 3, 61, 20, 24, 22, 53, 18,
     58, 56, 16, 44, 14, 5, 6, 19, 72, 46,
     49, 10, 42, 40, 46, 10, 6, 34, 17, 68,
     62, 34, 33, 68], 10))
