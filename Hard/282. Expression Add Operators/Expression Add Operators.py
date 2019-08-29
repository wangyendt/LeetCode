#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Expression Add Operators
@time: 2019/8/29 11:37
"""


class Solution:
    def addOperators(self, num: str, target: int) -> list:
        if len(num) == 0:
            return [''] if target == 0 else []
        v, val = num[0], int(num[0])
        dp = [[(val, v, val, val)]]
        for i in range(1, len(num)):
            v, val = num[i], int(num[i])
            dp_ = dp[-1]
            dp.append([])
            for e in dp_:
                dp[-1].append((e[0] + val, e[1] + '+' + v, val, val))
                dp[-1].append((e[0] - val, e[1] + '-' + v, val, -val))
                dp[-1].append((e[0] + e[3] * (val - 1), e[1] + '*' + v, val, e[3] * val))
                if e[2] == 0: continue
                f_head, f_tail = e[3] // e[2], e[2] * 10 + val
                dp[-1].append((e[0] - e[3] + f_head * f_tail, e[1] + v, f_tail, f_head * f_tail))
        return list(map(lambda e: e[1], filter(lambda e: e[0] == target, dp[-1])))


so = Solution()
print(so.addOperators('123', 6))
print(so.addOperators('232', 8))
print(so.addOperators('105', 5))
print(so.addOperators('00', 0))
print(so.addOperators('3456237490', 9191))
