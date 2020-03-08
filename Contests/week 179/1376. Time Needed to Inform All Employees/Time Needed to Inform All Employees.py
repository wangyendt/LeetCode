#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 20:55
@Author:  wang121ye
@File: Time Needed to Inform All Employees.py
@Software: PyCharm
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list, informTime: list) -> int:
        children = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)
