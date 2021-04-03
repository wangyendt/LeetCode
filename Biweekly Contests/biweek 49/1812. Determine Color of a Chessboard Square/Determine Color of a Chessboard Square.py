#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: 1
@time: 2021/04/03 22:28
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        map = {t: i + 1 for i, t in enumerate('abcdefgh')}
        res = []
        res.append(map[coordinates[0]])
        res.append(int(coordinates[1]))
        return (res[0] + res[1]) % 2 == 1
