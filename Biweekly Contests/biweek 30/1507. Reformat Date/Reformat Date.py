#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reformat Date
@time: 2020/07/11 22:30
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d, m, y = date.split(' ')
        d = d[:-2]
        if len(d) == 1:
            d = '0' + d
        m = str(months.index(m) + 1)
        if len(m) == 1:
            m = '0' + m
        return '-'.join((y, m, d))
