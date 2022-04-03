#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Scores of Built Strings.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def sumScores(self, s: str) -> int:
        def calculate_z_array(s):
            N = len(s)
            Z = [0] * N
            L, R = 0, 0
            for i in range(1, N):
                if i > R:
                    L = R = i
                    while R < N and s[R - L] == s[R]:
                        R += 1
                    R -= 1
                    Z[i] = R - L + 1
                else:
                    k = i - L
                    if Z[k] + i <= R:
                        Z[i] = Z[k]
                    else:
                        L = i
                        while R < N and s[R - L] == s[R]:
                            R += 1
                        R -= 1
                        Z[i] = R - L + 1
            return Z

        return sum(calculate_z_array(s)) + len(s)
