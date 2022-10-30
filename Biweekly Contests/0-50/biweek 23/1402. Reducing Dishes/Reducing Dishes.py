#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Reducing Dishes.py 
@time: 2020/04/08
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def maxSatisfaction(self, satisfaction: list) -> int:
        A = satisfaction
        A.sort()
        ret, cnt = 0, 0
        while A and A[-1] + cnt > 0:
            cnt += A.pop()
            ret += cnt
        return ret


so = Solution()
print(so.maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]))
print(so.maxSatisfaction(satisfaction=[4, 3, 2]))
print(so.maxSatisfaction(satisfaction=[-1, -4, -5]))
print(so.maxSatisfaction(satisfaction=[-2, 5, -1, 0, 3, -3]))
