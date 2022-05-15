#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Integers in Intervals.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import bisect


class CountIntervals:

    def __init__(self):
        self.interv = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:

        if not self.interv:
            self.interv += (left, right),
            self.cnt += right - left + 1
        else:
            li = bisect.bisect_left(self.interv, (left,))
            lval = left
            if li > 0 and left <= self.interv[li - 1][1] + 1:
                li -= 1
            if li < len(self.interv):
                lval = min(self.interv[li][0], lval)

            ri = bisect.bisect_right(self.interv, (right,))
            rval = right
            if ri < len(self.interv) and right >= self.interv[ri][0] - 1:
                ri += 1
            if ri > 0:
                rval = max(self.interv[ri - 1][1], rval)
            to_delete = 0
            for _ in range(li, ri):
                to_delete += self.interv[_][1] - self.interv[_][0] + 1
            self.cnt += rval - lval + 1 - to_delete
            self.interv[li: ri] = [(lval, rval)]

    def count(self) -> int:
        return self.cnt
