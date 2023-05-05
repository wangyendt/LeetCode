"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Maximum Number of Fish in a Grid.py
@time: 20230505
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections
from typing import *


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
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == n == 1: return grid[0][0]
        ufs = UnionFind(m * n + 1)
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    ufs.union(i * n + j, m * n)
                if j and grid[i][j] and grid[i][j - 1]:
                    ufs.union(i * n + j, i * n + j - 1)
                if i and grid[i][j] and grid[i - 1][j]:
                    ufs.union(i * n + j, (i - 1) * n + j)
        idxs = []
        for i in range(m * n + 1):
            idxs.append(ufs.find(i))
        res = collections.defaultdict(int)
        for i in range(len(idxs) - 1):
            p, q = i // n, i % n
            res[idxs[i]] += grid[p][q]
        # print(res)
        ret = 0
        for k, v in res.items():
            if k != idxs[-1]: ret = max(ret, v)
        return ret


so = Solution()
print(so.findMaxFish(grid=[[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
print(so.findMaxFish(grid=[[3]]))
print(so.findMaxFish(grid=[[0, 3]]))
print(so.findMaxFish(grid=[[3, 0]]))
print(so.findMaxFish(grid=[[3], [0]]))
print(so.findMaxFish(grid=[[10, 0], [0, 0]]))
