"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count Palindromic Subsequences.py
@time: 20221126
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections


class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7
        k = 10
        pairs = [[0 for _ in range(k ** 2)] for _ in range(n)]
        cnts = collections.defaultdict(int)
        int_s = [int(t) for t in s]
        for i in range(1, n - 2):
            if i >= 2:
                for j in range(k ** 2):
                    pairs[i - 1][j] = pairs[i - 2][j]
                    if j % k == int_s[i - 1]:
                        pairs[i - 1][j] += cnts[j // k]
                    pairs[i - 1][j] = pairs[i - 1][j] % mod
            cnts[int_s[i - 1]] += 1
        cnts = collections.defaultdict(int)
        ret = 0
        for i in range(n - 2, 1, -1):
            if i < n - 2:
                for j in range(k ** 2):
                    pairs[i + 1][j] = pairs[i + 2][j]
                    if j % k == int_s[i + 1]:
                        pairs[i + 1][j] += cnts[j // k]
                    pairs[i + 1][j] = pairs[i + 1][j] % mod
            cnts[int_s[i + 1]] += 1
            for k1 in range(k):
                for k2 in range(k):
                    ret += (pairs[i + 1][k1 * k + k2] * pairs[i - 1][k1 * k + k2]) % mod
        return ret % mod


so = Solution()
print(so.countPalindromes(s="103301"))
print(so.countPalindromes(s="0000000"))
print(so.countPalindromes(s="9999900000"))
print(so.countPalindromes(s="0110101001"))
