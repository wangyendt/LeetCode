#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Lowest Common Ancestor of Deepest Leaves.py 
@time: 2019/07/14
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root:
                return 0, None
            leftDep, left = helper(root.left)
            rightDep, right = helper(root.right)
            if leftDep > rightDep:
                ret = left
            elif leftDep < rightDep:
                ret = right
            else:
                ret = root
            return max(leftDep, rightDep) + 1, ret

        return helper(root)[1]
