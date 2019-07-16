# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 14:49
# software: PyCharm

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ret = []

        def helper(tree: TreeNode):
            if not tree:
                return
            else:
                ret.append(tree.val)
                helper(tree.left)
                helper(tree.right)

        helper(root)
        ret.sort()
        res = [abs(ret[i + 1] - ret[i]) for i in range(len(ret) - 1)]
        return min(res)
