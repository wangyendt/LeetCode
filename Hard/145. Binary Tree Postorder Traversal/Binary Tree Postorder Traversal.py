# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/9 11:50
# software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        stack = []
        ret = []
        while True:
            while root:
                # Push root's right child and then root to stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)

                # Set root as root's left child
                root = root.left

                # Pop an item from stack and set it as root
            root = stack.pop()

            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if root.right is not None and (stack[-1] if stack else None) == root.right:
                stack.pop()  # Remove right child from stack
                stack.append(root)  # Push root back to stack
                root = root.right  # change root so that the
                # right child is processed next

            # Else print root's data and set root as None
            else:
                ret.append(root.val)
                root = None

            if len(stack) <= 0:
                break
