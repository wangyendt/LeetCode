#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Day of the Year
@time: 2019/8/16 18:04
"""

from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        now = datetime.strptime(date, '%Y-%m-%d')
        last = datetime.strptime(date[:4], '%Y')
        return (now - last).days + 1


so = Solution()
print(so.dayOfYear('2004-03-01'))
