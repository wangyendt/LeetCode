#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Relative Sort Array.py 
@time: 2019/07/14
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        cnt = Counter(arr1)
        ret = []
        for a in arr2:
            ret.extend([a] * cnt[a])
            for i in range(cnt[a]):
                arr1.remove(a)
        arr1.sort()
        ret.extend(arr1)
        return ret


so = Solution()
print(so.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
