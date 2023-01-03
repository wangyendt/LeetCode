"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Closest Prime Numbers in Range.py
@time: 20230103
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *

import math


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num: int) -> bool:
            if num == 1:
                return False
            for divisor in range(2, math.floor(math.sqrt(num)) + 1):
                if num % divisor == 0:
                    return False
            return True

        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)

        gaps = ([primes[i - 1], primes[i]]
                for i in range(1, len(primes)))

        return min(gaps,
                   key=lambda gap: (gap[1] - gap[0], gap[0]),
                   default=[-1, -1])


so = Solution()
print(so.closestPrimes(left=1, right=1))
print(so.closestPrimes(left=10, right=19))
print(so.closestPrimes(left=12854, right=130337))
print(so.closestPrimes(left=618716, right=618799))
print(so.closestPrimes(left=710119, right=710189))
print(so.closestPrimes(left=981316, right=981373))
