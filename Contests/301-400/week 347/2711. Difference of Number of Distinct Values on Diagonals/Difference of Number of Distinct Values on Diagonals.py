"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Difference of Number of Distinct Values on Diagonals.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import itertools
from typing import *


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in itertools.product(range(m), range(n)):
            tl, br = set(), set()
            cur_i, cur_j = i - 1, j - 1
            while True:
                if 0 <= cur_i < m and 0 <= cur_j < n:
                    tl.add(grid[cur_i][cur_j])
                    cur_i -= 1
                    cur_j -= 1
                else:
                    break
            cur_i, cur_j = i + 1, j + 1
            while True:
                if 0 <= cur_i < m and 0 <= cur_j < n:
                    br.add(grid[cur_i][cur_j])
                    cur_i += 1
                    cur_j += 1
                else:
                    break
            ret[i][j] = abs(len(tl) - len(br))
        return ret


so = Solution()
print(so.differenceOfDistinctValues(grid=[[1, 2, 3], [3, 1, 5], [3, 2, 1]]))
