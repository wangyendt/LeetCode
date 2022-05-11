# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Clone Graph.py
@time: 2022/05/11
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

"""
# Definition for a Node.

"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


import collections


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        q, clones = collections.deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                cur_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]
