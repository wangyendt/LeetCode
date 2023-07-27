"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Prime Pairs With Target Sum.py
@time: 20230718
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def find_primes(m: int):
            primes = []
            is_prime = [True] * (m + 1)
            for i in range(2, m + 1):
                if is_prime[i]:
                    primes.append(i)
                    for j in range(2 * i, m + 1, i):
                        is_prime[j] = False
            return primes

        primes = set(find_primes(n))
        ret = []
        for i in range(2, n // 2 + 1):
            if i in primes and n - i in primes:
                ret.append([i, n - i])
        return ret


so = Solution()
print(so.findPrimePairs(999996))
