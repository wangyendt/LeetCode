"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Distinct Prime Factors of Product of Array.py
@time: 20230103
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        M = max(nums)

        def linear_sieve(n):
            prime = [True] * (n + 1)
            prime[0] = prime[1] = False
            for i in range(2, n + 1):
                if prime[i]:
                    for j in range(i * i, n + 1, i):
                        prime[j] = False
            return [i for i in range(2, n + 1) if prime[i]]

        primes = sorted(linear_sieve(M))
        for num in nums:
            for p in primes:
                if p > num:
                    break
                while num % p == 0:
                    s.add(p)
                    num //= p
        # print(primes)
        return len(s)


so = Solution()
print(so.distinctPrimeFactors(nums=[2, 4, 3, 7, 10, 6]))
