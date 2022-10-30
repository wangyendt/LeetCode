# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Add Minimum Number of Rungs.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pre = res = 0
        for a in rungs:
            res += (a - pre - 1) // dist
            pre = a
        return res
