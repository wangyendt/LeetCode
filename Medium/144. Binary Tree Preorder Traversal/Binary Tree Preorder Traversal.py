#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Binary Tree Preorder Traversal
@time: 2019/8/22 17:55
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root: return ret
        stack = [root]
        while stack:
            s = stack.pop()
            ret.append(s.val)
            if s.right:
                stack.append(s.right)
            if s.left:
                stack.append(s.left)
        return ret


so = Solution()
tree = parseTreeNode([1, 2, 3, 4, 5, 6, 7])
print(so.preorderTraversal(tree))
