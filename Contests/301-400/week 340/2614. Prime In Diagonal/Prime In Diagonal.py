#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Prime In Diagonal.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = len(nums)
        ret = 0

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        for i in range(N):
            if is_prime(nums[i][i]):
                ret = max(ret, nums[i][i])
            if is_prime(nums[i][~i]):
                ret = max(ret, nums[i][~i])
        return ret
