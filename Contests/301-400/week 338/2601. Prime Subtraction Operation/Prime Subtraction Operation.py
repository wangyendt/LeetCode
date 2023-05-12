"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Prime Subtraction Operation.py
@time: 20230512
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(num):
            prime = [True] * (num + 1)
            prime[0] = prime[1] = False

            for i in range(2, int(num ** 0.5) + 1):
                if prime[i]:
                    for j in range(i * i, num + 1, i):
                        prime[j] = False
            return [i for i in range(len(prime)) if prime[i]]

        primes = sieve(1000)
        n = len(nums)
        prev = 0
        for i in range(n):
            req = nums[i] - prev - 1
            idx = bisect.bisect_left(primes, req)
            takeCurr = False
            if idx >= len(primes) or primes[idx] > req:  # can't take from primes idx
                # check if we can take the prev idx bcz idx can't be taken idx-1 may be closest which satisfy the condition
                if idx > 0 and primes[idx - 1] <= req:
                    idx = idx - 1
                else:  # we have no choice need to take the curr element
                    takeCurr = True
            curr = nums[i]
            if not takeCurr:  # no need to take the curr element
                curr = nums[i] - primes[idx]
            if curr <= prev:  # if curr is not greater than prev can't make it
                return False
            prev = curr
        return True


so = Solution()
# print(so.primeSubOperation([5, 8, 3]))
print(so.primeSubOperation([998, 2]))
