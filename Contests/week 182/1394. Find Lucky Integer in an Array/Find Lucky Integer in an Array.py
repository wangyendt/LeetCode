#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Find Lucky Integer in an Array.py 
@time: 2020/04/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def findLucky(self, arr: list) -> int:
        return max([k for k, v in collections.Counter(arr).items() if k == v] or [-1])


so = Solution()
print(so.findLucky(arr=[2, 2, 3, 4]))
print(so.findLucky(arr=[1, 2, 2, 3, 3, 3]))
print(so.findLucky(arr=[2, 2, 2, 3, 3]))
print(so.findLucky(arr=[5]))
print(so.findLucky(arr=[7, 7, 7, 7, 7, 7, 7]))
