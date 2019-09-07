# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/7 13:26
# software: PyCharm


class Solution:
    def maximalSquare(self, A: list(list())) -> int:
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return len(A) and max(map(max, A)) ** 2


so = Solution()
print(so.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]
))
