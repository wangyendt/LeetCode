"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Smallest Value After Replacing With Sum of Prime Factors.py
@time: 20221218
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import functools


class Solution:
    def smallestValue(self, n: int) -> int:
        @functools.lru_cache(None)
        def get_prime_factors(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return factors

        m = n
        while True:
            res = get_prime_factors(m)
            # print(m, res)
            if len(res) == 1:
                return res[0]
            if m == sum(res):
                return m
            m = sum(res)


so = Solution()
print(so.smallestValue(4))
