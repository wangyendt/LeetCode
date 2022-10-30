# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Sum Obtained of Any Permutation.py
@time: 2020/09/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *

import numpy as np


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        res = np.zeros((n, 1))
        for rs, re in requests:
            res[rs:re + 1] += 1
        A = nums
        A.sort()
        B = [int(r[0]) for r in res]
        B.sort()
        return sum([a * b for a, b in zip(A, B)]) % (10 ** 9 + 7)


so = Solution()
# print(so.maxSumRangeQuery(nums=[1, 2, 3, 4, 5], requests=[[1, 3], [0, 1]]))
print(so.maxSumRangeQuery([1, 8, 5, 5, 2], [[4, 4], [3, 4], [4, 4], [2, 4], [0, 0]]))
