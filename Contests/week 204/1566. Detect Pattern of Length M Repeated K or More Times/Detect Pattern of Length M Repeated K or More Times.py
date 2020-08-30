#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Detect Pattern of Length M Repeated K or More Times.py 
@time: 2020/08/31
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def containsPattern(self, arr: list, m: int, k: int) -> bool:
        i = 0
        while i <= len(arr) - 1:
            p = arr[i:i + m]
            if p * k == arr[i:i + m * k]:
                return True
            i += 1
        return False

so = Solution()
print(so.containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(so.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(so.containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
print(so.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(so.containsPattern(arr=[2, 2, 2, 2], m=2, k=3))
