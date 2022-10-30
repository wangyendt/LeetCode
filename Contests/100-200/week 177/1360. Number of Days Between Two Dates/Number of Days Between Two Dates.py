#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Days Between Two Dates
@time: 2020/2/26 17:31
"""


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def date(s: str) -> int:
            y, m, d = map(int, s.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return y * 365 + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5

        return abs(date(date1) - date(date2))


so = Solution()
print(so.daysBetweenDates(date1="2019-06-29", date2="2019-06-30"))
print(so.daysBetweenDates(date1="2020-01-15", date2="2019-12-31"))
