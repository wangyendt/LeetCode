#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Validate Binary Tree Nodes
@time: 2020/2/26 17:47
"""


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list, rightChild: list) -> bool:
        return n - 1 == len([x for x in (leftChild + rightChild) if x != -1])


so = Solution()
print(so.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
