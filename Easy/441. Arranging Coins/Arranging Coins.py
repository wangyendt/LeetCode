# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/6 15:38
# software: PyCharm
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # (1+x)*x/2 <= n
        # x^2 + x - 2*n <= 0
        # x <= (-1 + sqrt(1+4*n)) / 2
        return int((-1 + math.sqrt(1 + 8 * n)) // 2)
