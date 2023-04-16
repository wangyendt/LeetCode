"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Width of Columns of a Grid.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ret = []
        for i in range(len(grid[0])):
            res = 0
            for j in range(len(grid)):
                res = max(res, len(str(grid[j][i])))
            ret.append(res)
        return ret
