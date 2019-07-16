# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 11:20
# software: PyCharm

class Solution:
    def convertToBase7(self, num: int) -> str:
        ret = ''
        if num == 0:
            return '0'
        m = abs(num)
        while m > 0:
            ret += str(m % 7)
            m //= 7
        if num > 0:
            return ret[::-1]
        else:
            return '-' + ret[::-1]


so = Solution()
print(so.convertToBase7(100))
print(so.convertToBase7(-16))
