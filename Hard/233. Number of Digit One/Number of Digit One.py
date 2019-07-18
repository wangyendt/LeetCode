# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/17 20:21
# software: PyCharm

class Solution:
    def countDigitOne(self, n):
        def digitCount(n, k):
            N, ret, dig = n, 0, 1
            while n >= 1:
                m, r = divmod(n, 10)
                if r > k:
                    ret += (m + 1) * dig
                elif r < k:
                    ret += m * dig
                elif r == k:
                    ret += m * dig + (N - n * dig + 1)
                n //= 10
                dig *= 10
            if k == 0:
                if N == 0:
                    return 1
                else:
                    return ret - dig // 10
            return ret

        return digitCount(n, 1)


so = Solution()
print(so.countDigitOne(855))
