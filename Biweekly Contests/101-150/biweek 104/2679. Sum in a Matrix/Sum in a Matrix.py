#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum in a Matrix.py 
@time: 2023/05/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import numpy as np


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        [num.sort() for num in nums]
        return np.array(nums).max(axis=0).sum()


so = Solution()
print(so.matrixSum(nums=[[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
