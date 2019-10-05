#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Longest Well-Performing Interval.py 
@time: 2019/07/14
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def longestWPI(self, hours: list) -> int:
        ret = 0
        cnt = 0
        seen = dict()
        for hi, h in enumerate(hours):
            if h > 8:
                cnt += 1
            else:
                cnt -= 1
            if cnt > 0:
                ret = hi + 1
            seen.setdefault(cnt, hi)
            if cnt - 1 in seen:
                ret = max(ret, hi - seen[cnt - 1])
        return ret


so = Solution()
print(so.longestWPI([9, 9, 6, 0, 6, 6, 9]))
print(so.longestWPI([9, 6, 6, 0, 6, 9, 9]))
print(so.longestWPI([6, 6, 6]))
print(so.longestWPI([9, 6, 9]))
