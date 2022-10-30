#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Array With Elements Not Equal to Average of Neighbors.py 
@time: 2021/08/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = []
        nums.sort()
        for i in range(n):
            if i & 1:
                ret.append(nums.pop())
            else:
                ret.append(nums.pop(0))
        return ret


so = Solution()
print(so.rearrangeArray(nums=[1, 1, 3, 4, 5]))
