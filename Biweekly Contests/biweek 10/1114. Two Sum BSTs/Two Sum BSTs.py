#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Two Sum BSTs.py 
@time: 2019/10/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        dic = dict()

        def helper(tree: TreeNode, target):
            if tree:
                dic[target - tree.val] = 1
                helper(tree.left, target)
                helper(tree.right, target)

        helper(root1, target)

        def helper2(tree: TreeNode):
            if tree and (tree.val in dic or helper2(tree.left) or helper2(tree.right)):
                return True
            return False

        return helper2(root2)


tree1 = parseTreeNode([0, -10, 10])
tree2 = parseTreeNode([5, 1, 7, 0, 2])
so = Solution()
print(so.twoSumBSTs(tree1, tree2, 17))
