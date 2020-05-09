#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 16:44
@Author:  wang121ye
@File: Max Difference You Can Get From Changing an Integer.py
@Software: PyCharm
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)
        if len(s_num) == 1: return 8
        for i, s in enumerate(s_num):
            if s != '9':
                a = s_num.replace(s, '9')
                break
        else:
            a = s_num
        a = int(a)
        if s_num[0] != '1':
            b = s_num.replace(s_num[0], '1')
        else:
            for i, s in enumerate(s_num):
                if s not in '01':
                    b = s_num.replace(s, '0')
                    break
            else:
                b = s_num
        b = int(b)
        return a - b


so = Solution()
print(so.maxDiff(555))
print(so.maxDiff(9))
print(so.maxDiff(123456))
print(so.maxDiff(10000))
print(so.maxDiff(9288))
