#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Subrectangle Queries
@time: 2020/06/13 22:30
"""


class SubrectangleQueries:

    def __init__(self, rectangle: list(list())):
        self.M = rectangle


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            for j in range(col1, col2+1):
                self.M[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.M[row][col]

