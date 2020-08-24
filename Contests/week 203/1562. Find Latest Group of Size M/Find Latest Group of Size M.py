#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Find Latest Group of Size M.py 
@time: 2020/08/24
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def findLatestStep(self, arr: list, m: int) -> int:
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res
