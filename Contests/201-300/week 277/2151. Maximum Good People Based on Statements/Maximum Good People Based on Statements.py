#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Good People Based on Statements.py 
@time: 2022/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        def fun(n, ans, c):  # this generate all the combination of 1 and 0 of lenght n.(simple recursion)
            if len(c) == n:
                ans.append(c)
                return
            p = c
            fun(n, ans, p + "1")
            fun(n, ans, c + "0")

        n = len(statements)
        ans = []
        c = ""
        fun(n, ans, c)
        res = 0
        for i in ans:
            g = i
            flag = True
            for j in range(n):
                if g[j] == "1":
                    # this is because we don't need to check for bad because he can lie also so we don't care about bad one.
                    for k in range(n):
                        if statements[j][k] != 2 and statements[j][k] != int(g[k]):
                            flag = False
                            break
                    if not flag:
                        break
            if flag:
                res = max(res, g.count("1"))
        return res
