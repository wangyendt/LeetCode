# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/6 18:02
# software: PyCharm


import itertools


class Solution:
    def combinationSum3(self, k: int, n: int) -> list(list()):
        return [a for a in itertools.combinations(list(range(1, 10)), k) if sum(a) == n]


so = Solution()
print(so.combinationSum3(3, 9))
