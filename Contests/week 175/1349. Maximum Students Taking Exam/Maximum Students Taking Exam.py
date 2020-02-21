#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Maximum Students Taking Exam
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:30
@Desc   ：
=================================================="""


class Solution(object):
    def maxStudents(self, A):
        R, C = len(A), len(A[0])
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val == '.':
                    A[r][c] = True
                else:
                    A[r][c] = False

        # dp on state transitions
        legal = [[] for _ in range(R)]
        for cand in itertools.product((0, 1), repeat=C):
            if any(cand[i] and cand[i + 1] for i in range(C - 1)):
                continue
            for r in range(R):
                if any(cand[i] and not A[r][i] for i in range(C)):
                    continue
                legal[r].append(cand)

        dp = {}
        for cand in legal[0]:
            dp[cand] = sum(cand)

        for r in range(1, R):
            dp2 = {}
            for cand, s in dp.items():
                for cand2 in legal[r]:
                    s2 = sum(cand2)
                    v2 = dp2.get(cand2, -1)
                    if v2 >= s + s2: continue
                    for i in range(C):
                        if cand[i]:
                            if i - 1 >= 0 and cand2[i - 1] or i + 1 < C and cand2[i + 1]:
                                break
                    else:
                        dp2[cand2] = s2 + s

            dp = dp2

        return max(dp.values())