"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Put Marbles in Bags.py
@time: 20230131
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        n = len(weights)
        s = []
        for i in range(n - 1):
            s.append(weights[i] + weights[i + 1])
        s.sort()
        return sum(s[-(k - 1):]) - sum(s[:(k - 1)])


so = Solution()
print(so.putMarbles(weights=[1, 3, 5, 1], k=2))
print(so.putMarbles([25, 74, 16, 51, 12, 48, 15, 5], 1))
