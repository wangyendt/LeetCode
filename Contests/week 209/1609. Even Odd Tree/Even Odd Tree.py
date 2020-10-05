#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Even Odd Tree
@time: 2020/10/05 09:01
"""

import collections
import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def helper(tree: TreeNode, lvl=0):
            if tree:
                if lvl % 2 == 0 and (tree.val % 2 == 0 or tree.val % 2 == 1 and res[lvl] and tree.val <= res[lvl][-1]):
                    return False
                elif lvl % 2 == 1 and (tree.val % 2 == 1 or tree.val % 2 == 0 and res[lvl] and tree.val >= res[lvl][-1]):
                    return False
                res[lvl].append(tree.val)
                return helper(tree.left, lvl + 1) and helper(tree.right, lvl + 1)
            return True

        res = collections.defaultdict(list)
        ret = helper(root)
        return ret


so = Solution()
tree = parseTreeNode([5, 9, 1, 3, 5, 7])
print(so.isEvenOddTree(tree))
