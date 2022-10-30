#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Stone Game IV
@time: 2020/07/11 22:51
"""

import math
import functools


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def dp(i):
            if i == (int(math.sqrt(i))) ** 2:
                return True
            else:
                for j in range(1, int(math.sqrt(i)) + 1)[::-1]:
                    if not dp(i - j ** 2):
                        return True
                return False

        return dp(n)


so = Solution()
# print(so.winnerSquareGame(1))
# print(so.winnerSquareGame(2))
print(so.winnerSquareGame(3))
# print(so.winnerSquareGame(4))
# print(so.winnerSquareGame(7))
# print(so.winnerSquareGame(17))
# print(so.winnerSquareGame(100000))
