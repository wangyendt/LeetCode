# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/5 11:11
# software: PyCharm


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


from collections import defaultdict


class Solution:
    def levelOrder(self, root: 'Node') -> list(list()):
        dic = defaultdict(list)

        def helper(root, level=0):
            if root:
                dic[level].append(root.val)
                for c in root.children:
                    helper(c, level + 1)
        helper(root)
        p = 0
        ret = []
        while True:
            if dic[p]:
                ret.append(dic[p])
            else:
                break
            p += 1
        return ret
