#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Substring of One Repeating Character.py 
@time: 2022/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class SegmentTree:
    def __init__(self, n, F):
        self.N = n
        self.F = F
        self.sums = [(0, 0, 0, 0, 0, 0) for i in range(2 * n)]
        self.dp = list(range(2 * n))
        for i in range(n - 1, -1, -1): self.dp[i] = self.dp[2 * i]

        L, R = self.N, 2 * self.N - 1
        parts = []
        while L <= R:
            if L & 1:
                parts += [(self.dp[L], L)]
                L += 1
            if R & 1 == 0:
                parts += [(self.dp[R], R)]
                R -= 1
            L //= 2;
            R //= 2

        parts.sort()
        self.d = [j for i, j in parts]

    def update(self, index, val):
        idx = index + self.N
        self.sums[idx] = (1, 1, 1, 1, val, val)
        while idx > 1:
            idx //= 2
            self.sums[idx] = self.F(self.sums[2 * idx], self.sums[2 * idx + 1])

    def query(self):
        ans = (0, 0, 0, 0, 0, 0)
        for x in self.d:
            ans = self.F(ans, self.sums[x])
        return ans


class Solution:
    def longestRepeating(self, s, Q1, Q2):
        def FN(a, b):
            if a == (0, 0, 0, 0, 0, 0): return b
            if b == (0, 0, 0, 0, 0, 0): return a
            f1, s1, e1, L1, r1, l1 = a
            f2, s2, e2, L2, r2, l2 = b
            if r1 == l2:
                return max(f1, f2, e1 + s2), s1 + s2 * (e1 == L1), e2 + e1 * (e2 == L2), L1 + L2, r2, l1
            else:
                return max(f1, f2), s1, e2, L1 + L2, r2, l1

        n = len(s)
        m = len(Q1)
        ans = []
        STree = SegmentTree(n, FN)
        for i in range(n):
            STree.update(i, s[i])
        for i in range(m):
            STree.update(Q2[i], Q1[i])
            ans += [STree.query()[0]]
        return ans
