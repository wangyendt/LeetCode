#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: The Number of Full Rounds You Have Played.py 
@time: 2021/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        h1, m1 = startTime.split(':')
        h2, m2 = finishTime.split(':')
        h1, h2, m1, m2 = int(h1), int(h2), int(m1), int(m2)
        if not (h1 < h2 or h1 == h2 and m1 <= m2):
            h2 += 24
        # print(h1, m1, h2, m2)
        if m1 % 15 != 0:
            m1 += 15 - m1 % 15
        if m2 % 15 != 0:
            m2 -= m2 % 15
        # print(f'{h1=},{m1=},{h2=},{m2=}')
        hd = h2 - h1
        md = m2 - m1
        d = hd * 60 + md
        return d // 15 if d > 0 else 0


so = Solution()
# print(so.numberOfRounds(startTime="12:01", finishTime="12:44"))
# print(so.numberOfRounds(startTime="12:29", finishTime="12:31"))
# print(so.numberOfRounds(startTime="12:16", finishTime="12:31"))
# print(so.numberOfRounds(startTime="12:14", finishTime="12:44"))
# print(so.numberOfRounds(startTime="12:14", finishTime="13:44"))
# print(so.numberOfRounds(startTime="00:00", finishTime="23:59"))
print(so.numberOfRounds("04:56", "04:55"))
