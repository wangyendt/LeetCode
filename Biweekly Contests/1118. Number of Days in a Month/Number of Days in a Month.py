#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Number of Days in a Month.py 
@time: 2019/07/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        retDict1 = {
            1: 31, 2: 28, 3: 31,
            4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31
        }
        retDict2 = {
            1: 31, 2: 29, 3: 31,
            4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31
        }
        if Y % 4 == 0:
            if Y % 100 == 0:
                if Y % 400 == 0:
                    return retDict2[M]
                else:
                    return retDict1[M]
            else:
                return retDict2[M]
        else:
            return retDict1[M]
