# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 17:19
# software: PyCharm

import heapq
import sys

sys.path.append('..')
from Tools.BinaryTree import *


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.heap = []

        def helper(tree: TreeNode):
            if tree:
                heapq.heappush(self.heap, tree.val)
                helper(tree.left)
                helper(tree.right)

        helper(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return heapq.heappop(self.heap)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.heap) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
