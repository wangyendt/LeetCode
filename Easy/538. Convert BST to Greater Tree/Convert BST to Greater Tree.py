# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 15:26
# software: PyCharm


import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution(object):
    def convertBST(self, root):
        def helper(tree, val):
            if not tree:
                return val
            val = helper(tree.right, val)
            tree.val += val
            return helper(tree.left, tree.val)

        helper(root, 0)
        return root


# tree = parseTreeNode([5, 2, 13])
tree = parseTreeNode([2, 0, 3, -4, 1])
so = Solution()
tree_ = so.convertBST(tree)
showTreeNode(tree_)
