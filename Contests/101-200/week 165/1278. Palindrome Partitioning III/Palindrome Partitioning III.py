#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Palindrome Partitioning III
@time: 2019/12/3 13:31
"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def num_changes(word):
            l, r = 0, len(word) - 1
            ret = 0
            while l < r:
                if word[l] != word[r]:
                    ret += 1
                l += 1
                r -= 1
            return ret

        def dp(ii, kk):
            if (ii, kk) not in memo:
                if kk == 1:
                    memo[(ii, kk)] = num_changes(s[:ii + 1])
                else:
                    memo[(ii, kk)] = min(dp(jj, kk - 1) + num_changes(s[jj + 1:ii + 1]) for jj in range(kk - 2, ii))
            return memo[(ii, kk)]

        memo = {}
        n = len(s)
        return dp(n - 1, k)


so = Solution()
print(so.palindromePartition(s="abc", k=2))
print(so.palindromePartition(s="aabbc", k=3))
print(so.palindromePartition(s="leetcode", k=8))
