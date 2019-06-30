#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Path In Zigzag Labelled Binary Tree.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def pathInZigZagTree(self, label: int) -> list:
        row, m = 0, label
        while m:
            row += 1
            m //= 2
        col = (label - 2 ** (row - 1)) if row % 2 else (2 ** row - label - 1)
        print(row, col)
        ret = []
        while row > 0:
            ret.append((2 ** (row - 1) + col) if row % 2 else (2 ** row - 1 - col))
            col //= 2
            row -= 1
        return ret[::-1]


so = Solution()
print(so.pathInZigZagTree(14), [1, 3, 4, 14])
