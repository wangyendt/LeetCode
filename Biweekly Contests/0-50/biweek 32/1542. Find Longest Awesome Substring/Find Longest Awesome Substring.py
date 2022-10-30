#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Find Longest Awesome Substring.py 
@time: 2020/08/09
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm
"""


class Solution:
    def longestAwesome(self, s):
        res, cur, n = 0, 0, len(s)
        seen = [-1] + [n] * 1024
        for i, c in enumerate(s):
            cur ^= 1 << int(c)
            for a in range(10):
                res = max(res, i - seen[cur ^ (1 << a)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res