"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Buy Two Chocolates.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if len(prices) < 2 or prices[0] + prices[1] > money:
            return money
        return money - prices[0] - prices[1]
