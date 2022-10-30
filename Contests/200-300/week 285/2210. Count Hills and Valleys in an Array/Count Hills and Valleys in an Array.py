#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Hills and Valleys in an Array.py 
@time: 2022/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if not res or res and res[-1] != n:
                res.append(n)
        ret = 0
        for i, r in enumerate(res):
            if 0 < i < len(res) - 1 and (res[i - 1] < r > res[i + 1] or res[i - 1] > r < res[i + 1]):
                # print(res[i - 1], r, res[i + 1], res[i - 1] < r > res[i + 1], res[i - 1] > r < res[i + 1])
                ret += 1
        return ret


so = Solution()
print(so.countHillValley([2, 4, 1, 1, 6, 5]))
print(so.countHillValley([6, 6, 5, 5, 4, 1]))
