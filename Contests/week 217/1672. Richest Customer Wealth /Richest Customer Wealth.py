#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Richest Customer Wealth
@time: 2020/11/29 12:02
"""

from typing import *


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(l) for l in accounts)
