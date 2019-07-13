# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 14:21
# software: PyCharm

import collections
import functools
import itertools
import operator as op

import math


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getFactors(n):
            cnt = collections.Counter()
            for i in range(2, int(math.sqrt(n)) + 1):
                while not n % i:
                    cnt[i] += 1
                    cnt[n // i] += 1
                    n //= i
            if not cnt:
                return sorted(list({1, n}))
            factors = [[k ** vi for vi in range(v + 1)] for k, v in cnt.items()]
            factors = sorted(list(set([functools.reduce(op.mul, r) for r in itertools.product(*factors)])))
            return factors

        ret, n = [], len(s)
        for fac in getFactors(n):
            if fac < n and s[:fac] * (n // fac) == s:
                return True
        return False


so = Solution()
print(so.repeatedSubstringPattern('abab'))
print(so.repeatedSubstringPattern('aba'))
