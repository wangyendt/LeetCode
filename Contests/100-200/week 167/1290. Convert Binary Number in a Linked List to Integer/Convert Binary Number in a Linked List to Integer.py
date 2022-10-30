#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Convert Binary Number in a Linked List to Integer
@time: 2019/12/16 17:25
"""

import sys

sys.path.append('..')
from Tools.LinkedList import *


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ''
        while head:
            res += str(head.val)
            head = head.next
        return int(res, 2)


so = Solution()
ll = LinkedList()
ll.append_list([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
print(so.getDecimalValue(ll.head))
