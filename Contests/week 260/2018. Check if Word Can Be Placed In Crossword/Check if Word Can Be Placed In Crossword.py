# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Check if Word Can Be Placed In Crossword.py
@time: 2021/09/26
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        B = board
        res = set()
        for i in range(m):
            start = False
            item = ''
            for j in range(n):
                if not start and B[i][j] not in '# ':
                    start = True
                    item += B[i][j]
                else:
                    if B[i][j] == '#':
                        if item:
                            res.add(item)
                        start = False
                        item = ''
                    else:
                        item += B[i][j]
            if item: res.add(item)
        for j in range(n):
            start = False
            item = ''
            for i in range(m):
                if not start and B[i][j] not in '# ':
                    start = True
                    item += B[i][j]
                else:
                    if B[i][j] == '#':
                        if item:
                            res.add(item)
                        start = False
                        item = ''
                    else:
                        item += B[i][j]
            if item: res.add(item)
        for r in res:
            if len(r) == len(word) and all(rr == ' ' or rr == word[i] for i, rr in enumerate(r)):
                return True
            if len(r) == len(word) and all(rr == ' ' or rr == word[i] for i, rr in enumerate(r[::-1])):
                return True
        return False


so = Solution()
print(so.placeWordInCrossword(board=[["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word="abc"))
