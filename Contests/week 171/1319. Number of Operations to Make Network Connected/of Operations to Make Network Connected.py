#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: of Operations to Make Network Connected
@time: 2020/1/15 16:21
"""

import sys

sys.path.append('..')
from Tools.UnionFindSet import *

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
    def makeConnected(self, n: int, connections: list(list())) -> int:
        if len(connections) < n - 1: return -1
        un = UnionFind(n)
        for conn in connections:
            un.union(conn[0], conn[1])
        return un.count() - 1


so = Solution()
print(so.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))
print(so.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
print(so.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))
print(so.makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]))
print(so.makeConnected(17,[[3,5],[8,12],[10,13],[2,4],[1,7],[6,11],[0,2],[1,5],[5,9],[1,3],[9,11],[2,12],[6,12],[4,10],[12,14],[3,6],[3,8]]))
