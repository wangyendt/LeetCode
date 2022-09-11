#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: SegmentTree.py 
@time: 2022/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class SegmentTreeRecursive:
    """
    Problem 2213
    """

    def __init__(self, n, arr):
        self.size = 1
        ZERO = (0, 0, 0, 0, 0, 0)
        while self.size < n:
            self.size *= 2
        self.T = [ZERO] * (2 * self.size - 1)
        self.arr = arr
        self.ZERO = ZERO  # neutral element

    def combine(self, a, b):
        f1, s1, e1, L1, r1, l1 = a
        f2, s2, e2, L2, r2, l2 = b
        f = max(f1, f2)
        if r1 == l2: f = max(f, e1 + s2)
        e = e2 + e1 if (e2 == L2 and r1 == l2) else e2
        s = s1 + s2 if (e1 == L1 and r1 == l2) else s1
        L = L1 + L2
        r = r2
        l = l1
        return (f, s, e, L, r, l)

    def one_element(self, x):
        return 1, 1, 1, 1, x, x

    def _build(self, x, lx, rx):
        if rx - lx == 1:
            if lx < len(self.arr):
                self.T[x] = self.one_element(self.arr[lx])
        else:
            mx = (lx + rx) // 2
            self._build(2 * x + 1, lx, mx)
            self._build(2 * x + 2, mx, rx)
            self.T[x] = self.combine(self.T[2 * x + 1], self.T[2 * x + 2])

    def build(self):
        self._build(0, 0, self.size)

    def _set(self, i, v, x, lx, rx):
        if rx - lx == 1:
            self.T[x] = self.one_element(v)
            return
        mx = (lx + rx) // 2
        if i < mx:
            self._set(i, v, 2 * x + 1, lx, mx)
        else:
            self._set(i, v, 2 * x + 2, mx, rx)
        self.T[x] = self.combine(self.T[2 * x + 1], self.T[2 * x + 2])

    def set(self, i, v):
        self._set(i, v, 0, 0, self.size)

    def _calc(self, l, r, x, lx, rx):
        if l >= rx or lx >= r:
            return self.ZERO
        if lx >= l and rx <= r:
            return self.T[x]
        mx = (lx + rx) // 2
        s1 = self._calc(l, r, 2 * x + 1, lx, mx)
        s2 = self._calc(l, r, 2 * x + 2, mx, rx)
        return self.combine(s1, s2)

    def calc(self, l, r):
        return self._calc(l, r, 0, 0, self.size)


class SegmentTreeIterative:
    """
    Problem 2213
    """

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


class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])
