#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Prime Arrangements.py 
@time: 2019/09/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def my_prime(n):
            is_prime = [True] * (n + 1)
            for i in range(2, (int(n ** 0.5) + 1)):
                if is_prime[i]:
                    for j in range(i ** 2, n + 1, i):
                        is_prime[j] = False
            return sum([1 for x in range(2, n) if is_prime[x]])

        def factorial(n):
            result = n
            for i in range(1, n):
                result = result * i
            return int(result)

        if n == 1: return 1
        num_primes = my_prime(n + 1)
        return (factorial(num_primes) * factorial(n - num_primes)) % 1000000007


so = Solution()
print(so.numPrimeArrangements(5))
print(so.numPrimeArrangements(100))
