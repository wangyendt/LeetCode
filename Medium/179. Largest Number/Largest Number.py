# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 17:28
# software: PyCharm

import functools


class Solution:
    def largestNumber(self, nums: list) -> str:
        str_nums = list(map(str, nums))
        str_nums.sort(key=functools.cmp_to_key(
            lambda x, y: int(str(x) + str(y)) - int(str(y) + str(x))
        ), reverse=True)
        return ''.join(str_nums).lstrip('0') or '0'


so = Solution()
print(so.largestNumber([10, 2]))
print(so.largestNumber([3, 30, 34, 5, 9]))
print(so.largestNumber([0, 0]))
print(so.largestNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]))
