#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Most Visited Sector in a Circular Track.py 
@time: 2020/08/24
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0] <= rounds[-1]:
            ret = range(rounds[0], rounds[-1] + 1)
        else:
            ret = list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1))
        ret = sorted(list(set(ret)))
        return ret
