# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 11:49
# software: PyCharm


from functools import reduce


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def get_all_factors(n: int) -> list:
            return list(set(reduce(list.__add__,
                                   ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))

        return sum(get_all_factors(num)) == 2 * num


so = Solution()
print(so.checkPerfectNumber(28))
