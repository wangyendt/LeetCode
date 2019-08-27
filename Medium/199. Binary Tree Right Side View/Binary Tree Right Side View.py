# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/27 11:41
# software: PyCharm


import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        dict = {}

        def helper(tree: TreeNode, level=0):
            if not tree: return
            dict[level] = tree.val
            helper(tree.left, level + 1)
            helper(tree.right, level + 1)
        helper(root)
        return list(dict.values())


tree = parseTreeNode([1, 2, 3, 'null', 5, 'null', 4])
so = Solution()
so.rightSideView(tree)
