# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/25 11:36
# software: PyCharm


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def backtrack(_dp, _s1, _s2, i, j):
            if i == 0 or j == 0:
                return []
            if _s1[i - 1] == _s2[j - 1]:
                return backtrack(_dp, _s1, _s2, i - 1, j - 1) + [(i - 1, j - 1)]
            if _dp[i][j - 1] > _dp[i - 1][j]:
                return backtrack(_dp, _s1, _s2, i, j - 1)
            return backtrack(_dp, _s1, _s2, i - 1, j)

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if dp[-1][-1] == 0:
            return str1 + str2
        lcsInd = backtrack(dp, str1, str2, len(str1), len(str2))
        # print([str1[i[0]] for i in lcsInd])
        # print(lcsInd)
        ret = list(str1)
        p = len(str2) - 1
        while p >= 0:
            if lcsInd:
                if p > lcsInd[-1][1]:
                    ret.insert(lcsInd[-1][0] + 1, str2[p])
                elif p == lcsInd[-1][1]:
                    lcsInd.pop()
            else:
                ret.insert(0, str2[p])
            p -= 1
        return ''.join(ret)


so = Solution()
print(so.shortestCommonSupersequence(str1="abac", str2="cab"))
print(so.shortestCommonSupersequence("bbbaaaba", "bbababbb"))
