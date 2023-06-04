#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Semi-Ordered Permutation.py 
@time: 2023/06/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        mn, mx = 1, len(nums)
        mni, mxi = nums.index(mn), nums.index(mx)
        # print(mni, mxi)
        if mni < mxi:
            return mni + (len(nums) - 1 - mxi)
        else:
            return mni + (len(nums) - 1 - mxi) - 1


so = Solution()
print(so.semiOrderedPermutation(nums=[2, 1, 4, 3]))
