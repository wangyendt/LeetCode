# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/20 12:12
# software: PyCharm


class Solution:
    def balancedString(self, s: str) -> int:
        A = ['QWER'.index(c) for c in s]
        N = len(A)
        counts = [0, 0, 0, 0]
        P = [counts[:]]
        for x in A:
            counts[x] += 1
            P.append(counts[:])

        T = len(A) // 4

        if counts[0] == counts[1] == counts[2] == counts[3] == T:
            return 0

        def possible(size):
            for i in range(N - size + 1):
                j = i + size
                # P[j] - P[i] is what is deleted
                # remaining is counts - P[j] + P[i]
                for d in range(4):
                    if counts[d] - P[j][d] + P[i][d] > T:
                        break
                else:
                    return True
            return False

        lo = 0
        hi = N
        while lo < hi:  # inv: possible for N
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


so = Solution()
# print(so.balancedString("QQWE"), 1)
# print(so.balancedString("QWER"), 0)
# print(so.balancedString("QQQW"), 2)
# print(so.balancedString("QQQQ"), 3)
# print(so.balancedString("WQWRQQQW"), 3)
print(so.balancedString("WWEQERQWQWWRWWERQWEQ"), 4)
