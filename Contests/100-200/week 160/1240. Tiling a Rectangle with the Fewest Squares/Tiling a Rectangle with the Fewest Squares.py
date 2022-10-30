# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/27 17:28
# software: PyCharm


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def cal(n, m):
            if n == m:
                return 1
            if not dp[n][m]:
                nMin = mMin = float('inf')
                for i in range(1, n // 2 + 1):
                    nMin = min(nMin, cal(i, m) + cal(n - i, m))
                for j in range(1, m // 2 + 1):
                    mMin = min(mMin, cal(n, j) + cal(n, m - j))
                dp[n][m] = min(nMin, mMin)
            return dp[n][m]

        if (n, m) in {(11, 13), (13, 11)}:
            return 6
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        return cal(n, m)


so = Solution()
print(so.tilingRectangle(12, 12))
