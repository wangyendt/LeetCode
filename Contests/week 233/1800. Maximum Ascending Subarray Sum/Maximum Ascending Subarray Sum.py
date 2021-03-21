#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Ascending Subarray Sum.py 
@time: 2021/03/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        last = 0
        ret = 0
        s = 0
        for n in nums:
            ret = max(ret, n)
            if n > last:
                s += n
                ret = max(ret, s)
            else:
                s = n
            last = n
        return ret
