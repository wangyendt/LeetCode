#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Number of Ways to Split a String.py 
@time: 2020/09/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def numWays(self, s: str) -> int:
        n = sum(1 for i in s if i == '1')
        if n == 0: return ((len(s) - 1) * (len(s) - 2) // 2) % (10 ** 9 + 7)
        if n % 3 != 0: return 0
        f1 = f2 = f3 = f4 = False
        i1 = i2 = i3 = i4 = 0
        k = n // 3
        cur = 0
        for i in range(len(s)):
            if s[i] == '1':
                cur += 1
            if not f1 and cur == k:
                i1 = i
                f1 = True
            if not f2 and cur == k + 1:
                i2 = i
                f2 = True
            if not f3 and cur == 2 * k:
                i3 = i
                f3 = True
            if not f4 and cur == 2 * k + 1:
                i4 = i
                f4 = True
        return ((i2 - i1) * (i4 - i3)) % (10 ** 9 + 7)


so = Solution()
print(so.numWays(s="10101"))
