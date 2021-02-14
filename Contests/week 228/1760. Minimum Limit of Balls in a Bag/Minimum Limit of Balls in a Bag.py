# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Minimum Limit of Balls in a Bag.py
@time: 2021/02/14
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import math
from typing import *
import bisect


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        A, k = nums, maxOperations
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) / 2
            if sum((a - 1) / mid for a in A) > k:
                left = mid + 1
            else:
                right = mid
        return left


so = Solution()
# print(so.minimumSize([9], 2))
# print(so.minimumSize([2, 4, 8, 2], 4))
# print(so.minimumSize([7, 17], 2))
print(so.minimumSize(
    [431, 922, 158, 60, 192, 14, 788, 146, 788, 775, 772, 792, 68, 143, 376, 375, 877, 516, 595, 82, 56, 704, 160, 403, 713, 504, 67, 332, 26], 80))
