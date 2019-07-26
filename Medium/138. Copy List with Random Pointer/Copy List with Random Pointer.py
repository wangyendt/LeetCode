# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/22 19:53
# software: PyCharm

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
import copy


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)
