# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/19 18:29
# software: PyCharm

# Definition for a binary tree node.
from Tools.BinaryTree import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        error = []

        def recursive(tree, out=False):
            if tree:
                if out:
                    l, r = tree.right, tree.left
                else:
                    l, r = tree.left, tree.right
                for child in recursive(l, out):
                    yield child
                yield tree
                for child in recursive(r, out):
                    yield child

        if not root:
            return
        parent = None
        for child in recursive(root, False):
            print(child.key)
            if parent and parent.key > child.key:
                error.append(parent)
                break
            parent = child
        parent = None
        for child in recursive(root, True):
            print(child.key)
            if parent and parent.key < child.key:
                error.append(parent)
                break
            parent = child
        error[0].key, error[1].key = error[1].key, error[0].key


tree = parseTreeNode([1, 3, 'null', 'null', 2])
tree = parseTreeNode([3, 1, 4, 'null', 'null', 2])

so = Solution()
print(showTreeNode(tree))
so.recoverTree(tree)
print(showTreeNode(tree))
