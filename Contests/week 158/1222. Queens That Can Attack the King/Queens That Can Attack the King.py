#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Queens That Can Attack the King.py 
@time: 2019/10/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def queensAttacktheKing(self, queens: list(list()), king: list()) -> list(list()):
        kx, ky = king
        ret = []
        for i in range(kx - 1, -1, -1):
            if [i, ky] in queens:
                ret.append([i, ky])
                break
        for i in range(kx + 1, 8):
            if [i, ky] in queens:
                ret.append([i, ky])
                break
        for j in range(ky - 1, -1, -1):
            if [kx, j] in queens:
                ret.append([kx, j])
                break
        for j in range(ky + 1, 8):
            if [kx, j] in queens:
                ret.append([kx, j])
                break
        px, py = kx - 1, ky - 1
        while px >= 0 and py >= 0:
            if [px, py] in queens:
                ret.append([px, py])
                break
            px -= 1
            py -= 1
        px, py = kx - 1, ky + 1
        while px >= 0 and py < 8:
            if [px, py] in queens:
                ret.append([px, py])
                break
            px -= 1
            py += 1
        px, py = kx + 1, ky - 1
        while px < 8 and py >= 0:
            if [px, py] in queens:
                ret.append([px, py])
                break
            px += 1
            py -= 1
        px, py = kx + 1, ky + 1
        while px < 8 and py < 8:
            if [px, py] in queens:
                ret.append([px, py])
                break
            px += 1
            py += 1
        return ret


so = Solution()
print(so.queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))
print(so.queensAttacktheKing([[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]))
print(so.queensAttacktheKing(
    queens=[[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4],
            [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2],
            [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], king=[3, 4]))
