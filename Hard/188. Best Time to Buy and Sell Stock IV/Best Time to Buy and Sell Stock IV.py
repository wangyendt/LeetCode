# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/11 11:46
# software: PyCharm
import sys


class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        if k == 0 or not prices: return 0
        if k > len(prices) // 2:
            ret = 0
            for pi in range(len(prices) - 1):
                if prices[pi + 1] > prices[pi]:
                    ret += prices[pi + 1] - prices[pi]
            return ret
        buyers, sellers = [-sys.maxsize] * k, [-sys.maxsize] * k
        for p in prices:
            for j in range(k):
                buyers[j] = max(buyers[j], -p + (0 if j == 0 else sellers[j - 1]))
                sellers[j] = max(sellers[j], p + buyers[j])
                if j > 0 and buyers[j] == buyers[j - 1] and sellers[j] == sellers[j - 1]:
                    break
        for s in sellers[::-1]:
            if s > -sys.maxsize:
                return s


so = Solution()
print(so.maxProfit(0, [1, 3]))
print(so.maxProfit(20, [3, 2, 6, 5, 0, 3]))
