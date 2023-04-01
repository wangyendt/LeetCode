"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Make K-Subarray Sums Equal.py
@time: 20230401
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import math


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        gcd = math.gcd(n, k)
        ans = 0
        for i in range(gcd):
            tmp = sorted([arr[j] for j in range(i, n, gcd)])
            median = tmp[len(tmp) // 2]
            ans += sum(abs(num - median) for num in tmp)
        return ans


so = Solution()
print(so.makeSubKSumEqual(arr=[1, 4, 1, 3], k=2))
print(so.makeSubKSumEqual(arr=[2, 5, 5, 7], k=3))
print(so.makeSubKSumEqual([2, 10, 9], 1))
print(so.makeSubKSumEqual([7, 3, 10, 6], 2))
