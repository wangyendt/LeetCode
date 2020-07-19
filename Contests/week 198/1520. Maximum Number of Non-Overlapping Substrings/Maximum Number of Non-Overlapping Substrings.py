#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Non-Overlapping Substrings
@time: 2020/07/20 01:45
"""


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list:
        tmp = {c: [s.index(c), s.rindex(c) + 1] for c in set(s)}
        # find all the correct boundries
        pairs = []
        for c in set(s):
            l = tmpl = s.index(c)
            r = tmpr = s.rindex(c) + 1
            while True:
                t = set(s[tmpl:tmpr])
                for k in t:
                    tmpl = min(tmpl, tmp[k][0])
                    tmpr = max(tmpr, tmp[k][1])
                if (tmpl, tmpr) == (l, r):
                    break
                l, r = tmpl, tmpr
            pairs.append([l, r])

        # greedily find the optimal solution
        # similar to find the maximum number of meetings
        pairs.sort(key=lambda x: x[1])
        res, last = [], 0
        for b, e in pairs:
            if b >= last:
                res.append(s[b:e])
                last = e
        return res
