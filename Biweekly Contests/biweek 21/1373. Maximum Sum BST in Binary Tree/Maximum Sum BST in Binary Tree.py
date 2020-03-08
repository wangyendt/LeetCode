#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 20:14
@Author:  wang121ye
@File: Maximum Sum BST in Binary Tree.py
@Software: PyCharm
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0

        def traverse(root):
            '''return status_of_bst, size_of_bst, left_bound, right_bound'''
            nonlocal res
            if not root: return 1, 0, None, None  # this subtree is empty

            ls, l, ll, lr = traverse(root.left)
            rs, r, rl, rr = traverse(root.right)

            if ((ls == 2 and lr < root.val) or ls == 1) and ((rs == 2 and rl > root.val) or rs == 1):
                # this subtree is a BST
                size = root.val + l + r
                res = max(res, size)
                return 2, size, (ll if ll is not None else root.val), (rr if rr is not None else root.val)
            return 0, None, None, None  # this subtree is not a BST

        traverse(root)
        return res
