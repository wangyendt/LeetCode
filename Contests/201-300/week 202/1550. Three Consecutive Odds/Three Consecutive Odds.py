#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Three Consecutive Odds
@time: 2020/08/16 23:45
"""


class Solution:
    def threeConsecutiveOdds(self, arr: list) -> bool:
        cnt = 0
        for a in arr:
            if a % 2:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False
