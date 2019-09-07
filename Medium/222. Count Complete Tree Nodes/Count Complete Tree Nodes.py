# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/7 13:49
# software: PyCharm


import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ret = [0]

        def helper(tree):
            if tree:
                ret[0] = ret[0] + 1
                helper(tree.left)
                helper(tree.right)

        helper(root)
        return ret[0]
