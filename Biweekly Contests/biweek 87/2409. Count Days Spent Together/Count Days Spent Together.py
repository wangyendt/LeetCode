#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Days Spent Together.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        presum = [0]
        for day in days:
            presum.append(presum[-1] + day)

        def date2days(date: str):
            month, day = date.split('-')
            month = int(month)
            day = int(day)
            return presum[month - 1] + day

        return max(0, min(date2days(leaveAlice), date2days(leaveBob)) - max(date2days(arriveAlice), date2days(arriveBob)) + 1)
