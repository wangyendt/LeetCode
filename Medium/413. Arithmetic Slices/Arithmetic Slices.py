# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Arithmetic Slices.py
@time: 2021/08/10
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        diff.append(100000)
        res = []
        last = 10000
        cnt = 1
        for i, d in enumerate(diff):
            if d == last:
                cnt += 1
            else:
                if cnt != 1:
                    res.append(cnt + 1)
                cnt = 1
            last = d
        ret = 0
        for r in res:
            ret += (r - 2) * (r - 1) // 2
        return ret
