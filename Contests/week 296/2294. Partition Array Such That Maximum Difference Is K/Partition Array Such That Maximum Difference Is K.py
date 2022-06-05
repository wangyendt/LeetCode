#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Partition Array Such That Maximum Difference Is K.py 
@time: 2022/06/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        stack = [0]
        for i, n in enumerate(nums):
            if i:
                if n - nums[stack[-1]] <= k:
                    continue
                else:
                    stack.append(i)
        return len(stack)


so = Solution()
print(so.partitionArray(nums=[3, 6, 1, 2, 5], k=2))
