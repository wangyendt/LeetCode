#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Unreachable Pairs of Nodes in an Undirected Graph.py 
@time: 2022/06/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class UnionFind:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.

    This module implements an union find or disjoint set data structure.

    An union find data structure can keep track of a set of elements into a number
    of disjoint (non overlapping) subsets. That is why it is also known as the
    disjoint set data structure. Mainly two useful operations on such a data
    structure can be performed. A *find* operation determines which subset a
    particular element is in. This can be used for determining if two
    elements are in the same subset. An *union* Join two subsets into a
    single subset.

    The complexity of these two operations depend on the particular implementation.
    It is possible to achieve constant time (O(1)) for any one of those operations
    while the operation is penalized. A balance between the complexities of these
    two operations is desirable and achievable following two enhancements:

    1.  Using union by rank -- always attach the smaller tree to the root of the
        larger tree.
    2.  Using path compression -- flattening the structure of the tree whenever
        find is used on it.
    """

    def __init__(self, N):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """

        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        """Find the set identifier for the item p."""

        id = self._id
        while p != id[p]:
            id[p] = p = id[id[p]]  # Path compression using halving.
        return p

    def count(self):
        """Return the number of items."""

        return self._count

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not."""

        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Combine sets containing p and q into a single set."""

        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def is_percolate(self):
        return len(self._id) == 1

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for e1, e2 in edges:
            uf.union(e1, e2)
        res = collections.defaultdict(int)
        for i in range(n):
            res[uf.find(i)] += 1
        # print(res)
        ret = n * (n - 1) // 2
        for v in res.values():
            ret -= v * (v - 1) // 2
        return ret


so = Solution()
print(so.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
