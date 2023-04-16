"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Cousins in Binary Tree II.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections
from typing import *
import sys

sys.path.append('..')
from Tools.BinaryTree import *


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.level_sum = collections.defaultdict(int)

        def helper(tree: TreeNode, level=0):
            if tree:
                self.level_sum[level] += tree.val
                helper(tree.left, level + 1)
                helper(tree.right, level + 1)

        def modify(tree: TreeNode, level=0):
            if level == 0: tree.val = 0
            if tree:
                left = right = 0
                if tree.left:
                    if tree.right:
                        left = self.level_sum[level + 1] - tree.right.val - tree.left.val
                        right = self.level_sum[level + 1] - tree.left.val - tree.right.val
                    else:
                        left = self.level_sum[level + 1] - tree.left.val
                else:
                    if tree.right:
                        right = self.level_sum[level + 1] - tree.right.val
                if tree.left:
                    tree.left.val = left
                if tree.right:
                    tree.right.val = right
                modify(tree.left, level + 1)
                modify(tree.right, level + 1)

        helper(root)
        modify(root)
        return root


null = 'null'
root = [5, 4, 9, 1, 10, null, 7]
root_tree = parseTreeNode(root)
so = Solution()
root_ans = so.replaceValueInTree(root_tree)
print(showTreeNode(root_ans))
