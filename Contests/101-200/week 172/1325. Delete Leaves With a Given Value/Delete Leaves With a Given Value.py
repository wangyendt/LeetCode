#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Delete Leaves With a Given Value
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/27 13:20
@Desc   ：
=================================================="""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def helper(tree: TreeNode):
            if not tree: return 1
            l = helper(tree.left)
            if l == 1: tree.left = None
            r = helper(tree.right)
            if r == 1: tree.right = None
            if not tree.left and not tree.right and tree.val == target: return 1
            return 0

        helper(root)
        if root and root.val == target and not root.left and not root.right: return None
        return root


null = 'null'
root = [1, 2, 3, 2, null, 2, 4]
target = 2
root = [1, 3, 3, 3, 2]
target = 3
root = parseTreeNode(root)
so = Solution()
print(showTreeNode(so.removeLeafNodes(root, target)))
