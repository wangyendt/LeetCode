# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/5 11:21
# software: PyCharm

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def pathSum(self, root, sum):

        self.count = 0

        def dfs(node, path):
            if node:
                for i in range(len(path)):
                    path[i] += node.val
                path += node.val,
                for i in path:
                    if i == sum:
                        self.count += 1
                dfs(node.left, path[:])
                dfs(node.right, path[:])

        dfs(root, [])
        return self.count


so = Solution()
l = [10, 5, -3, 3, 2, 'null', 11, 3, -2, 'null', 1]
tree = parseTreeNode(l)
print(so.pathSum(tree, 8))
