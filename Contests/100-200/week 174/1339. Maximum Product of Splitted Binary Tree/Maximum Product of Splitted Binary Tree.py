#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Maximum Product of Splitted Binary Tree
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:19
@Desc   ：
=================================================="""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def get_sum(tree: TreeNode):
            if tree:
                return tree.val + get_sum(tree.left) + get_sum(tree.right)
            return 0

        all_sum = get_sum(root)
        ret = [float('-inf')]

        def helper(tree: TreeNode):
            if tree.left:
                l = helper(tree.left)
                ret[0] = max(ret[0], l * (all_sum - l))
            else:
                l = 0
            if tree.right:
                r = helper(tree.right)
                ret[0] = max(ret[0], r * (all_sum - r))
            else:
                r = 0
            return l + r + tree.val

        helper(root)
        return int(ret[0]) % (10 ** 9 + 7)
