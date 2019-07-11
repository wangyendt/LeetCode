# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/19 22:40
# software: PyCharm

class Solution:
    def maxProfit(self, prices: list) -> int:
        buy1, buy2, sell1, sell2 = float('-inf'), float('-inf'), 0, 0
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2


so = Solution()
print(so.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 6)
