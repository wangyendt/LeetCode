# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 10:58
# software: PyCharm

import sys

sys.path.append('..')
from Tools.BinaryTree import *
import collections


class Solution:
    def findMode(self, root: TreeNode) -> list:
        arr = []
        if not root: return []

        def helper(tree: TreeNode):
            if tree:
                arr.append(tree.val)
                helper(tree.left)
                helper(tree.right)

        helper(root)
        cnter = sorted(((k, v) for k, v in collections.Counter(arr).items()), key=lambda x: x[1])
        return [c[0] for c in cnter if c[1] == cnter[-1][1]]


null = 'null'
tree = parseTreeNode([1, null, 2, 2])
so = Solution()
print(so.findMode(tree))
