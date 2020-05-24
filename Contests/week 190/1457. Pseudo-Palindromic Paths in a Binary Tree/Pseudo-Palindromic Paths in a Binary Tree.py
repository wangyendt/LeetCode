#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/24 10:54
@Author:  wang121ye
@File: Pseudo-Palindromic Paths in a Binary Tree.py
@Software: PyCharm
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *
import collections


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        ret = [0]

        def helper(tree: TreeNode, cnt: collections.Counter):
            if tree:
                # print(tree.val)
                cnt[tree.val] += 1
                if tree.left or tree.right:
                    helper(tree.left, cnt.copy())
                    helper(tree.right, cnt.copy())
                else:
                    # print(cnt)
                    cur = 0
                    for k in range(1, 10):
                        if cnt[k] % 2 == 1:
                            cur += 1
                    if cur <= 1:
                        ret[0] = ret[0] + 1

        helper(root, collections.Counter())
        return ret[0]


so = Solution()
null = 'null'
tree = parseTreeNode([2, 3, 1, 3, 1, null, 1])
print(so.pseudoPalindromicPaths(tree))
tree = parseTreeNode([2, 1, 1, 1, 3, null, null, null, null, null, 1])
print(so.pseudoPalindromicPaths(tree))
tree = parseTreeNode([9])
print(so.pseudoPalindromicPaths(tree))
