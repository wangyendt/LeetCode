#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 17:21
@Author:  wang121ye
@File: Check If All 1's Are at Least Length K Places Away.py
@Software: PyCharm
"""


class Solution:
    def kLengthApart(self, nums: list, k: int) -> bool:
        N, last = len(nums), -1
        for i, c in enumerate(nums):
            if c == 1 and last == -1:
                last = i
                continue
            if c == 1 and last != -1:
                if i - last <= k:
                    return False
                last = i
                continue
        return True


so = Solution()
print(so.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(so.kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
print(so.kLengthApart(nums=[1, 1, 1, 1, 1], k=0))
print(so.kLengthApart(nums=[0, 1, 0, 1], k=1))
