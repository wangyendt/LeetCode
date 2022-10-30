#!/usr/bin/python
# coding: utf-8
# @Time    : 2022/2/6 2:23
# @Author  : Ye Wang (Wayne)
# @Email   : wang121ye@hotmail.com
# @File    : Partition Array According to Given Pivot.py
# @Software: PyCharm


from typing import *


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, pivots, right = [], [], []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n == pivot:
                pivots.append(n)
            elif n > pivot:
                right.append(n)
        return left + pivots + right
