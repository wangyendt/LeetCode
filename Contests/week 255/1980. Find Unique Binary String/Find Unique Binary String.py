#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Unique Binary String.py
@time: 2021/08/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        m = 2 ** n
        ns = set(nums)
        for i in range(m):
            s = bin(i)[2:]
            if len(s) < n:
                s = '0' * (n - len(s)) + s
            if s not in ns:
                return s


so = Solution()
print(so.findDifferentBinaryString(nums=["01", "10"]))
