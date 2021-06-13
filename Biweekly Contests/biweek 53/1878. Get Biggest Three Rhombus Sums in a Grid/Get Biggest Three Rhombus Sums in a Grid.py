#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Get Biggest Three Rhombus Sums in a Grid.py 
@time: 2021/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ret = set()
        m, n = len(grid), len(grid[0])

        def update(ele):
            ret.add(ele)

        for i in range(m):
            for j in range(n):
                update(grid[i][j])
        pre1 = dict()
        for i in range(m + n - 1):
            if i < m:
                stx, sty = i, 0
            else:
                stx, sty = m - 1, i + 1 - m
            res = 0
            pre1[i] = dict()
            while True:
                pre1[i][(stx, sty)] = (res, res + grid[stx][sty])
                res += grid[stx][sty]
                stx -= 1
                sty += 1
                if not (0 <= stx < m and 0 <= sty < n):
                    break
        pre2 = dict()
        for i in range(m + n - 1):
            if i < m:
                stx, sty = m - 1 - i, 0
            else:
                stx, sty = 0, i + 1 - m
            res = 0
            pre2[i] = dict()
            while True:
                pre2[i][(stx, sty)] = (res, res + grid[stx][sty])
                res += grid[stx][sty]
                stx += 1
                sty += 1
                if not (0 <= stx < m and 0 <= sty < n):
                    break
        for r in range(1, min((m + 1) // 2, (n + 1) // 2)):
            for ci in range(r, m - r):
                for cj in range(r, n - r):
                    top = (ci - r, cj)
                    bottom = (ci + r, cj)
                    left = (ci, cj - r)
                    right = (ci, cj + r)
                    ntl = ci + cj - r
                    nrb = ci + cj + r
                    if ci + r >= cj:
                        nbl = m - 1 - (ci + r - cj)
                    else:
                        nbl = m - 1 + cj - (ci + r)
                    if ci - r >= cj:
                        ntr = m - 1 - (ci - r - cj)
                    else:
                        ntr = m - 1 + cj - (ci - r)
                    # pprint.pprint(pre2)
                    # print(m, n, ci, cj, r, top, right)
                    # print(ntr)
                    res = 0
                    res += pre1[ntl][top][1] - pre1[ntl][left][0]
                    res += pre1[nrb][right][1] - pre1[nrb][bottom][0]
                    res += pre2[nbl][bottom][1] - pre2[nbl][left][0]
                    res += pre2[ntr][right][1] - pre2[ntr][top][0]
                    res -= grid[ci - r][cj] + grid[ci + r][cj] + grid[ci][cj - r] + grid[ci][cj + r]
                    update(res)
        ret2 = []
        for i in range(3):
            if not ret: break
            res = max(ret)
            ret2.append(res)
            ret.remove(res)
        return ret2


so = Solution()
print(so.getBiggestThree(
    grid=[[3, 4, 5, 1, 3],
          [3, 3, 4, 2, 3],
          [20, 30, 200, 40, 10],
          [1, 5, 5, 4, 1],
          [4, 3, 2, 2, 5]]
))
print(so.getBiggestThree([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(so.getBiggestThree(
    [[20, 17, 9, 13, 5, 2, 9, 1, 5],
     [14, 9, 9, 9, 16, 18, 3, 4, 12],
     [18, 15, 10, 20, 19, 20, 15, 12, 11],
     [19, 16, 19, 18, 8, 13, 15, 14, 11],
     [4, 19, 5, 2, 19, 17, 7, 2, 2]]
))
