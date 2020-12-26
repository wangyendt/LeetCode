#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Students Unable to Eat Lunch
@time: 2020/12/27 00:25
"""

from typing import *


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1 = sum(1 for stu in students if stu == 1)
        s2 = len(students) - s1
        c1 = c2 = 0
        for i, sw in enumerate(sandwiches):
            if sw == 0:
                c2 += 1
                if c2 == s2 + 1:
                    return len(sandwiches) - i
            if sw == 1:
                c1 += 1
                if c1 == s1 + 1:
                    return len(sandwiches) - i
        return 0
