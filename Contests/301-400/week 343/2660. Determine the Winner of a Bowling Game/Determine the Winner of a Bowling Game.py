"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Determine the Winner of a Bowling Game.py
@time: 20230506
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1 = s2 = 0
        for i, p1 in enumerate(player1):
            if i >= 2 and player1[i - 2] == 10 or i >= 1 and player1[i - 1] == 10:
                s1 += 2 * p1
            else:
                s1 += p1
        for i, p2 in enumerate(player2):
            if i >= 2 and player2[i - 2] == 10 or i >= 1 and player2[i - 1] == 10:
                s2 += 2 * p2
            else:
                s2 += p2
        if s1 == s2:
            return 0
        elif s1 > s2:
            return 1
        else:
            return 2
