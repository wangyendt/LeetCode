#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Delete Tree Nodes
@time: 2019/12/2 14:26
"""

import collections


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: list, value: list) -> int:
        children = collections.defaultdict(list)
        for i, n in enumerate(parent):
            children[n].append(i)

        def helper(i_tree):
            s = 0
            N = 1
            for child in children[i_tree]:
                if child != -1:
                    n_nodes, n_sum = helper(child)
                    N += n_nodes
                    s += n_sum
            s += value[i_tree]
            if s == 0:
                return 0, 0
            else:
                return N, s

        return helper(0)[0]


so = Solution()
print(so.deleteTreeNodes(nodes=7, parent=[-1, 0, 0, 1, 2, 2, 2], value=[1, -2, 4, 0, -2, -1, -1]))
print(so.deleteTreeNodes(7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -2]))
