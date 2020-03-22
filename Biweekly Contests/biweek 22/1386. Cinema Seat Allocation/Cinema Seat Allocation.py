#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/22 23:14
@Author:  wang121ye
@File: Cinema Seat Allocation.py
@Software: PyCharm
"""


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list(list())) -> int:
        res = 0
        occupies = {}
        for x, y in reservedSeats:
            if x not in occupies:
                occupies[x] = [y]
            else:
                occupies[x] += [y]
        res += (n - len(occupies)) * 2
        for k, v in occupies.items():
            if v == [1] or v == [10] or v == [1, 10] or v == [10, 1]:
                res += 2
                continue
            if 2 not in v and 3 not in v and 4 not in v and 5 not in v:
                res += 1
            elif 4 not in v and 5 not in v and 6 not in v and 7 not in v:
                res += 1
            elif 6 not in v and 7 not in v and 8 not in v and 9 not in v:
                res += 1
        return res


so = Solution()
print(so.maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(so.maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
print(so.maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))
