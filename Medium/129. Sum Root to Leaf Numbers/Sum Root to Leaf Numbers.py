# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/6 16:57
# software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ret = 0

        def dfs(tree, pathSum):
            if not tree:
                return
            cur = pathSum * 10 + tree.val
            if not (tree.left or tree.right):
                self.ret += cur
            else:
                dfs(tree.left, cur)
                dfs(tree.right, cur)

        dfs(root, 0)
        return self.ret
