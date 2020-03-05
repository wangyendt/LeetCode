#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Linked List in Binary Tree
@time: 2020/3/5 14:25
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *
from Tools.LinkedList import *


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def helper(llA: ListNode, trB: TreeNode):
            if not llA: return True
            if not trB: return False
            return llA.val == trB.val and (helper(llA.next, trB.left) or helper(llA.next, trB.right))

        if not head: return True
        if not root: return False
        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
