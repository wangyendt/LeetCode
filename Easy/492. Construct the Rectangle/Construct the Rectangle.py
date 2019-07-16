# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/15 14:30
# software: PyCharm

import math


class Solution:
    def constructRectangle(self, area: int) -> list:
        w = int(math.sqrt(area))
        while w >= 1:
            if area % w == 0:
                l = area // w
                return [l, w]
            w -= 1


so = Solution()
print(so.constructRectangle(100))
