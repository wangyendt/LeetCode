# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 17:08
# software: PyCharm


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = (numerator < 0) ^ (denominator < 0)
        w, r = divmod(abs(numerator), abs(denominator))
        s = str(w)
        if sign:
            s = "-" + s
        if r:
            s += '.'
        i = len(s)
        nums = {r: i}
        while r:
            q, r = divmod(r * 10, abs(denominator))
            s += str(q)
            if r in nums:
                s = s[:nums[r]] + '(' + s[nums[r]:] + ')'
                return s
            i += 1
            nums[r] = i
        return s
