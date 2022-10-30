#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 10:30
@Author:  wang121ye
@File: Number of Students Doing Homework at a Given Time.py
@Software: PyCharm
"""


class Solution:
    def busyStudent(self, startTime: list, endTime: list, queryTime: int) -> int:
        ret = 0
        for i, j in zip(startTime, endTime):
            if i <= queryTime <= j:
                ret += 1
        return ret


so = Solution()
print(so.busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))
print(so.busyStudent(startTime=[4], endTime=[4], queryTime=4))
print(so.busyStudent(startTime=[4], endTime=[4], queryTime=5))
print(so.busyStudent(startTime=[1, 1, 1, 1], endTime=[1, 3, 2, 4], queryTime=7))
print(so.busyStudent(startTime=[9, 8, 7, 6, 5, 4, 3, 2, 1], endTime=[10, 10, 10, 10, 10, 10, 10, 10, 10], queryTime=5))
