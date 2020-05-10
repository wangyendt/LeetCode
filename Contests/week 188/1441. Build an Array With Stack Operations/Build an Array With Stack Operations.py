#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/10 23:24
@Author:  wang121ye
@File: Build an Array With Stack Operations.py
@Software: PyCharm
"""


class Solution:
    def buildArray(self, target: list, n: int) -> list:
        ret = []
        pt = 1
        while target:
            t = target[0]
            while pt < t:
                ret.append('Push')
                ret.append('Pop')
                pt += 1
            ret.append('Push')
            target.pop(0)
            pt += 1
        return ret


so = Solution()
print(so.buildArray(target=[1, 3], n=3))
print(so.buildArray(target=[1, 2, 3], n=3))
print(so.buildArray(target=[1, 2], n=4))
print(so.buildArray(target=[2, 3, 4], n=4))
