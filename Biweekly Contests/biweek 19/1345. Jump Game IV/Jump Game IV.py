#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Jump Game IV
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/22 3:34
@Desc   ：
=================================================="""

import collections
import itertools


class Solution:
    def minJumps(self, A: list) -> int:
        indices = collections.defaultdict(list)
        for i, a in enumerate(A):
            indices[a].append(i)
        done, now = {-1}, {0}
        for steps in itertools.count():
            done |= now
            if len(A) - 1 in done:
                return steps
            now = {j for i in now for j in [i - 1, i + 1] + indices.pop(A[i], [])} - done


so = Solution()
print(so.minJumps(A=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
print(so.minJumps(A=[7]))
print(so.minJumps(A=[7, 6, 9, 6, 9, 6, 9, 7]))
print(so.minJumps(A=[6, 1, 9]))
print(so.minJumps(A=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
