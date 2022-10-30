#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize Number of Nice Divisors.py 
@time: 2021/03/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        M = 10 ** 9 + 7
        n = primeFactors
        if n <= 3: return n
        if n % 3 == 0: return pow(3, n // 3, M)
        if n % 3 == 1: return (pow(3, (n - 4) // 3, M) * 4) % M
        return (2 * pow(3, n // 3, M)) % M
