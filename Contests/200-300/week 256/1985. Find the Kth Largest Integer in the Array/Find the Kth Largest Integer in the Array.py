#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Kth Largest Integer in the Array.py 
@time: 2021/08/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=lambda x: int(x), reverse=True)[k - 1]


so = Solution()
print(so.kthLargestNumber(['12' * 65] * 10000, 9999))
