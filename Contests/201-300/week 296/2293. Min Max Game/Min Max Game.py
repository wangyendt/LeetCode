#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Min Max Game.py 
@time: 2022/06/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ret = []
        for i in range(len(nums) // 2):
            if i % 2 == 0:
                ret.append(min(nums[i * 2], nums[i * 2 + 1]))
            else:
                ret.append(max(nums[i * 2], nums[i * 2 + 1]))
        return self.minMaxGame(ret)
