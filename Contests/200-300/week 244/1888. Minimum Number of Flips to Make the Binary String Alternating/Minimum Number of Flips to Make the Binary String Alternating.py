#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Flips to Make the Binary String Alternating.py 
@time: 2021/06/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        res = [0] * n
        for i in range(n):
            res[i] = 1 if s[i] == '1' else 0
        o1 = [0] * (n + 1)
        e1 = [0] * (n + 1)
        for i in range(n):
            if i & 1:
                if res[i] == 1:
                    o1[i + 1] = o1[i] + 1
                else:
                    o1[i + 1] = o1[i] + 0

                if res[i] == 0:
                    e1[i + 1] = e1[i] + 1
                else:
                    e1[i + 1] = e1[i] + 0
            else:
                if res[i] == 0:
                    o1[i + 1] = o1[i] + 1
                else:
                    o1[i + 1] = o1[i] + 0

                if res[i] == 1:
                    e1[i + 1] = e1[i] + 1
                else:
                    e1[i + 1] = e1[i] + 0

        minimum = min(o1[n], e1[n])

        for i in range(n):
            if n & 1:
                minimum = min(minimum, o1[n] - o1[i + 1] + e1[i + 1])
                minimum = min(minimum, e1[n] - e1[i + 1] + o1[i + 1])
        return minimum
