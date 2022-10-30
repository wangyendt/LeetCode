#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Number of Distinct Integers After Reverse Operations.py 
@time: 2022/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for n in nums:
            nums_set.add(int(str(n)[::-1]))
        return len(nums_set)


so = Solution()
print(so.countDistinctIntegers(nums=[1, 13, 10, 12, 31]))
