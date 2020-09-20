# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Sum of All Odd Length Subarrays.py
@time: 2020/09/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = 0
        n = len(arr)
        if n % 2 == 1:
            m = n
        else:
            m = n - 1
        for i in range(1, m + 1, 2):
            for j in range(n):
                if j + i <= n:
                    ret += sum(arr[j:j + i])

        return ret


so = Solution()
print(so.sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]))
