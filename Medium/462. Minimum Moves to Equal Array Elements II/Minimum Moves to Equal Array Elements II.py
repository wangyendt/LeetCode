# !/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author: Ye Wang (Wayne)
@license: MIT Licence 
@file: Minimum Moves to Equal Array Elements II.py 
@time: 2022/06/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs
"""

from typing import *


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = nums[n // 2]
        return sum(abs(num - m) for num in nums)
