#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Booking Concert Tickets in Groups.py 
@time: 2022/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class SegmentTree():
    def __init__(self, l, r):
        self.val = 0
        self.mid = (l + r) // 2
        self.l = l
        self.r = r
        self.left, self.right = None, None
        self.max = 0
        self.sums = 0
        if l != r:
            self.left = SegmentTree(l, self.mid)
            self.right = SegmentTree(self.mid + 1, r)

    def update(self, l, r, val=1):
        if self.l >= l and self.r <= r:
            self.val += val
            self.max += val
            self.sums += val * (r - l + 1)
            return
        if self.l > r or self.r < l:
            return

        self.left.update(l, r, val)
        self.right.update(l, r, val)
        self.max = self.val + max(self.left.max, self.right.max)
        self.sums = self.val * (self.r - self.l + 1) + self.left.sums + self.right.sums

    def query(self, i):
        if self.l == self.r and self.l == i:
            return self.val
        if i < self.l or i > self.r:
            return 0
        if i <= self.mid:
            return self.val + self.left.query(i)
        return self.val + self.right.query(i)

    def querySum(self, l, r):
        # return sum value in range [l,r]
        if self.l >= l and self.r <= r:
            return self.sums
        if self.l > r or self.r < l:
            return 0
        return self.val * (min(r, self.r) - max(l, self.l) + 1) + self.left.querySum(l, r) + self.right.querySum(l, r)

    def queryLowestGreater(self, v):
        # return the smallest row that remain seats greater than v
        if self.max < v:
            return -1
        if self.l == self.r:
            return -1 if self.max < v else self.l
        if self.left.max >= v - self.val:
            return self.left.queryLowestGreater(v - self.val)
        return self.right.queryLowestGreater(v - self.val)


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.st = SegmentTree(0, n - 1)
        self.st.update(0, n - 1, m)
        self.m = m
        self.k = 0
        self.n = n

    def gather(self, k: int, maxRow: int):
        i = self.st.queryLowestGreater(k)
        if i < 0 or i > maxRow:
            return []
        v = self.st.query(i)
        self.st.update(i, i, -k)
        return [i, self.m - v]

    def scatter(self, k: int, maxRow: int):
        # if sum 0_maxRow greater than k,it's possible to book
        if self.st.querySum(0, maxRow) >= k:
            # book seats from lowest row
            while self.k < self.n and k > 0:
                v = self.st.query(self.k)
                self.st.update(self.k, self.k, -min(v, k))
                if v > k:
                    break
                else:
                    k -= v
                    self.k += 1
            return True
        return False
