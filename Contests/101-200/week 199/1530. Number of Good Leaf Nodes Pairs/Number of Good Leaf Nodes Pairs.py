#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Good Leaf Nodes Pairs
@time: 2020/07/27 01:06
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *
# import bisect


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ret = 0

        def helper(tree: TreeNode) -> list:
            if not tree:
                return []
            elif not tree.left and not tree.right:
                return [1]
            else:
                left = helper(tree.left)
                right = helper(tree.right)
                for l in left:
                    for r in right:
                        if l + r <= distance:
                            self.ret += 1
                return [e + 1 for e in left + right]

        helper(root)
        return self.ret


null = 'null'
so = Solution()
tree = parseTreeNode([1, 2, 3, null, 4])
print(so.countPairs(tree, 3))
tree = parseTreeNode([1, 2, 3, 4, 5, 6, 7])
print(so.countPairs(tree, 3))
tree = parseTreeNode([7, 1, 4, 6, null, 5, 3, null, null, null, null, null, 2])
print(so.countPairs(tree, 3))
tree = parseTreeNode([100])
print(so.countPairs(tree, 1))
tree = parseTreeNode([1, 1, 1])
print(so.countPairs(tree, 2))
print(so.countPairs(parseTreeNode(
    [38, 41, 59, 51, 5, 32, 51, 56, 64, 55, 6, 57, 80, 61, 50, 9, 81, 73, 89, 97, 17, 26, 16, 65, 63, 28, 24, 58, 48,
     22, 52, 81, 9, 43, 60, 49, 70, 30, 71, 6, 74, 53, 15, 32, 85, 46, 39, 47, 6, 80, 85, 40, null, 7, 94, 6, 17, 13,
     81, 7, 67, 78, 56, 34, 29, 45, 57, 20, 32, 28, 57, 82, 43, 7, 28, 3, 54, 15, 58, 8, 77, 62, 76, 93, 33, 80, 22, 21,
     76, 5, 31, 40, 81, 67, 13, 94, 14, 7, 53, 46, 90, 32, null, 89, 52, 63, null, null, 10, 93, 13, 22, 58, 92, null,
     30, null, 44, null, 21, null, null, null, null, null, 86, 21, 90, 90, 21, 45, 66, 9, 81, 44, 95, null, 69, 85,
     null, 63, 15, 71, null, 97, 24, 22, 5, 94, 100, null, 24, null, 11, 45, null, 43, 24, 66, 16, null, null, 56, 56,
     null, 33, 22, 36, null, null, null, null, 5, 13, 18, 26, 20, 51, null, null, null, 17, 98, null, 29, null, 50, 86,
     null, 66, 59, null, null, 28, null, null, null, 10, null, null, 62, 77, null, 64, 94, null, 77, 6, null, null,
     null, 80, 97, 74, 3, null, 72, null, null, null, null, null, null, 100, 64, null, 48, null, 58, 49, 78, 93, null,
     99, null, 14, 99, null, null, 19, null, null, 87, null, null, 33, null, null, null, null, 11, 51, null, 81, 76,
     null, 63, 28, 36, null, null, 10, 48, 13, null, null, 19, null, null, null, null, null, 57, null, null, null, null,
     null, null, 68, null, 34, 3, null, null, 47, 15, 68, null, null, null, 34, null, 92, null, null, null, null, null,
     null, null, null, null, null, null, 95, null, null, null, null, null, null, null, null, null, null, null, 61, 54,
     null, null, null, 76, 39, null, null, null, null, null, null, 61, 83, null, null, null, null, null, null, 36, null,
     null, 28, null, 37, null, null, null, 34, null, null, null, null, null, 6, null, 97, 23, null, null, 30, null,
     null, null, null, null, 17, null, null, null, null, null, null, null, null, null, 78, null, null, null, null, null,
     null, null, null, null, 66, null, null, 63, null, null, null, null, null, null, null, null, null, null, null, 7,
     null, null, null, null, null, 28, null, null, null, null, null, null, null, null, null, null, null, null, 39, null,
     null, null, null, null, null, null, null, null, 10, null, null, null, null, null, null, null, null, 36, null, 90]),
    7))
