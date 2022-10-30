# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Minimum Degree of a Connected Trio in a Graph.py
@time: 2021/02/14
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        connect = [[0 for _ in range(n)] for _ in range(n)]
        for e in edges:
            connect[e[0] - 1][e[1] - 1] = 1
            connect[e[1] - 1][e[0] - 1] = 1
        count = [0] * n
        for i in range(n):
            count[i] = connect[i].count(1)
        ans = -1
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if connect[i][j] and connect[j][k] and connect[k][i]:
                        if ans == -1:
                            ans = count[i] + count[j] + count[k] - 6
                        else:
                            ans = min(ans, count[i] + count[j] + count[k] - 6)
        return ans
