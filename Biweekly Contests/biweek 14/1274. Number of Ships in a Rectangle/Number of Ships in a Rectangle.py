#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Ships in a Rectangle
@time: 2019/12/2 15:07
"""


class Solution(object):
    def countShips(self, sea: 'Sea', tr: 'Point', bl: 'Point') -> int:
        ret = 0
        if tr.x >= bl.x and tr.y >= bl.y and sea.hasShips(tr, bl):
            if tr.x == bl.x and tr.y == bl.y:
                return 1
            mx, my = (tr.x + bl.x) // 2, (tr.y + bl.y) // 2
            ret += self.countShips(sea, tr, Point(mx + 1, my + 1))
            ret += self.countShips(sea, Point(mx, my), bl)
            ret += self.countShips(sea, Point(mx, tr.y), Point(bl.x, my + 1))
            ret += self.countShips(sea, Point(tr.x, my), Point(mx + 1, bl.y))
        return ret
