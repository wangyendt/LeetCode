#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of k-Mirror Numbers.py 
@time: 2021/11/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def fn(x):
            """Return next k-symmetric number."""
            s = list(x)
            n = len(s) // 2
            for i in range(n, len(s)):
                if int(s[i]) + 1 < k:
                    s[i] = s[~i] = str(int(s[i]) + 1)
                    for ii in range(n, i): s[ii] = s[~ii] = '0'
                    return "".join(s)
            return "1" + "0" * (len(s) - 1) + "1"

        x = "0"
        ans = 0
        for _ in range(n):
            x = fn(x)
            val = int(x, k)
            while str(val)[::-1] != str(val):
                x = fn(x)
                val = int(x, k)
            ans += val
        return ans
