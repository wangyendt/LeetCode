#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Serialize and Deserialize Binary Tree
@time: 2019/8/29 16:53
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        ret = []

        def helper(tree: TreeNode, ind=0):
            if not tree: return
            ret.append({ind: tree.val})
            helper(tree.left, 2 * ind + 1)
            helper(tree.right, 2 * ind + 2)

        helper(root)
        return str(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ele_dict = {}
        data = data.replace('[', '').replace(']', '').replace('{', '').replace('}', '').split(',')
        if '' in data: return None
        for d in data:
            k, v = d.split(':')
            ele_dict[int(k)] = int(v)

        def helper(ind=0):
            if ind in ele_dict:
                tree = TreeNode(ele_dict[ind])
                tree.left = helper(2 * ind + 1)
                tree.right = helper(2 * ind + 2)
                return tree
            return None

        return helper()


encoder = Codec()
tree = parseTreeNode([1, 2, 3, 'null', 'null', 6, 7])
# tree = parseTreeNode([])
res = encoder.serialize(tree)
print(res)
decoded_tree = encoder.deserialize(res)
print(showTreeNode(decoded_tree))
