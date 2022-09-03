#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Strictly Palindromic Number.py 
@time: 2022/09/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def f(n, x):
            # n为待转换的十进制数，x为机制，取值为2-16
            a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
            b = []
            while True:
                s = n // x  # 商
                y = n % x  # 余数
                b.append(y)
                b = b + [y]
                if s == 0:
                    break
                n = s
            for i in range(len(b) // 2):
                if b[i] != b[~i]:
                    return False
            return True

        for x in range(2, n - 1):
            if not f(n, x):
                return False
        return True


so = Solution()
print(so.isStrictlyPalindromic(9))
