#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Intersection of Three Sorted Arrays.py 
@time: 2019/10/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def arraysIntersection(self, arr1: list, arr2: list, arr3: list) -> list:
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))


so = Solution()
print(so.arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]))
