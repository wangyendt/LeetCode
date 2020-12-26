#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Average Waiting Time
@time: 2020/12/27 00:26
"""

from typing import *


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0
        last_end = 0
        for cus in customers:
            start, spend = cus[0], cus[1]
            last_end = max(last_end, start) + spend
            wait_time += last_end - start
        return wait_time / len(customers)
