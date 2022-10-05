#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize XOR.py 
@time: 2022/10/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_1(n):
            n_ones = 0
            while n:
                n &= (n - 1)
                n_ones += 1
            return n_ones

        n1, n2 = count_1(num1), count_1(num2)
        if n1 == n2: return num1
        b1 = bin(num1)[2:]
        # print(b1, n1, n2)
        if n1 > n2:
            r = n1 - n2
            for i in range(len(b1))[::-1]:
                if b1[i] == '1':
                    b1 = b1[:i] + '0' + b1[i + 1:]
                    # b1[i] = '0'
                    r -= 1
                    if r == 0: break
            return int(b1, 2)
        elif n2 > n1:
            n2 -= n1
            for i in range(len(b1))[::-1]:
                if b1[i] == '0':
                    b1 = b1[:i] + '1' + b1[i + 1:]
                    n2 -= 1
                    if n2 == 0:
                        break
            b1 = '1' * n2 + b1
            return int(b1, 2)


so = Solution()
print(so.minimizeXor(3, 5))
print(so.minimizeXor(1, 12))
print(so.minimizeXor(25, 31))
