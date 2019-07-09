# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/9 15:37
# software: PyCharm

from collections import Counter


class Solution:
    def maxPoints(self, points: list(list())) -> int:
        def gcd(v1, v2):
            if v1 < v2:
                v1, v2 = v2, v1
            rem = v1 % v2
            if rem == 0:
                return v2
            return gcd(rem, v2)

        m = len(points)
        if m <= 1:
            return m
        ret = 0
        for j in range(m):
            path = Counter()
            for i in range(m):
                if i != j:
                    x, y = points[j][0] - points[i][0], points[j][1] - points[i][1]
                    if x == 0 and y == 0:
                        path[(0, 0)] += 1
                    elif x == 0:
                        path[(0, 1)] += 1
                    elif y == 0:
                        path[(1, 0)] += 1
                    else:
                        g = gcd(abs(x), abs(y))
                        x, y = x // g, y // g
                        if x < 0:
                            x, y = -x, -y
                        path[(x, y)] += 1
            n = path[(0, 0)]
            for k in path.keys():
                if k != (0, 0):
                    path[k] += n
            mc = path.most_common()
            if mc:
                ret = max(ret, path.most_common()[0][1] + 1)
        return ret


so = Solution()
# print(so.maxPoints([[1, 1], [2, 2], [3, 3], [3, 3]]))
# print(so.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
print(so.maxPoints([[0, 0]]))
print(so.maxPoints([[0, 0], [0, 0]]))
print(so.maxPoints([[0, 0], [0, 0], [0, 0]]))
