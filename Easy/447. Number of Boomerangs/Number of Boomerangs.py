# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 11:17
# software: PyCharm
import operator as op
from collections import Counter
from functools import reduce


class Solution:
    def numberOfBoomerangs(self, points: list(list())) -> int:
        def nPr(n, r):
            r = min(r, n - r)
            numer = reduce(op.mul, range(n, 0, -1), 1)
            denom = reduce(op.mul, range(1, r + 1, 1), 1)
            return numer // denom

        ret = 0
        if not points:
            return ret
        n = len(points)
        for i in range(n):
            cnt = Counter()
            for j in range(n):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    cnt[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            for c in cnt:
                if cnt[c] > 1:
                    ret += nPr(cnt[c], 2)
        return ret


so = Solution()
print(so.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
print(so.numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]))
