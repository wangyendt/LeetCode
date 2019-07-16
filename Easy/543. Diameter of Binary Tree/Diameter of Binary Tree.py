# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 19:24
# software: PyCharm


import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ret = [0]

        def helper(tree):
            if not tree:
                return 0
            left, right = helper(tree.left), helper(tree.right)
            ret[0] = max(ret[0], left + right)
            return 1 + max(left, right)

        helper(root)
        return ret[0]
