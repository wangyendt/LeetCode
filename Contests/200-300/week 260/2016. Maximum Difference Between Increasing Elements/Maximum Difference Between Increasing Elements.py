# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Difference Between Increasing Elements.py
@time: 2021/09/26
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    ret = max(ret, nums[j] - nums[i])
        return ret
