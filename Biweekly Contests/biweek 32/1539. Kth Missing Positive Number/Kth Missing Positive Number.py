#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Kth Missing Positive Number.py 
@time: 2020/08/09
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        p, cnt = 1, 0
        arr = set(arr)
        while True:
            if p not in arr:
                cnt += 1
            if cnt == k:
                return p
            p += 1
