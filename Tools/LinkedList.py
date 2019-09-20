#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: LinkedList
@time: 2019/8/22 17:09
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    # 判断链表是否为空
    def is_empty(self):
        return self.length == 0

    # 插入节点this_node
    def append(self, this_node):
        if isinstance(this_node, ListNode):
            pass
        else:
            this_node = ListNode(this_node)
        if self.is_empty():
            self.head = this_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = this_node
        self.length += 1

    def append_list(self, arr):
        for a in arr:
            self.append(a)

    # 在第index处插入节点this_node
    def insert(self, this_node, index):
        if index > self.length:
            return 'Error'
        if isinstance(this_node, ListNode):
            pass
        else:
            this_node = ListNode(this_node)
        if index == 0:
            this_node.next = self.head
            self.head = this_node
        else:
            p = self.head
            while index - 1:
                p = p.next
                index -= 1
            this_node.next = p.next
            p.next = this_node
        self.length += 1

    # 删除第index个节点
    def delete(self, index):
        if not 0 <= index < self.length:
            return 'Error'
        if index == 0:
            self.head = self.head.next
        else:
            p = self.head
            while index - 1:
                p = p.next
                index -= 1
            p.next = p.next.next
        self.length -= 1

    # 更新第index节点的值
    def update(self, data, index):
        if not 0 <= index < self.length:
            return 'Error'
        if index == 0:
            self.head.data = data
        else:
            p = self.head
            while index:
                p = p.next
                index -= 1
            p.data = data

    # 获取第index节点的值
    def get_data(self, index):
        if not 0 <= index < self.length:
            return 'Error'
        if index == 0:
            return self.head.data
        else:
            p = self.head
            while index:
                p = p.next
                index -= 1
            return p.data

    # 获取链表长度
    def get_length(self):
        return self.length

    # 清空链表
    def clear(self):
        self.head = None
        self.length = 0

    # 打印链表
    def print_list(self):
        self.print_list_node(self.head)

    @classmethod
    def print_list_node(cls, list_node: ListNode):
        linked_list = LinkedList()
        head = list_node
        while head:
            linked_list.append(head.val)
            # print(list_node.val, '↓')
            head = head.next
            # print(list_node.val, '↑')
        if linked_list.length == 0:
            return None
        else:
            p = linked_list.head
            while p.next:
                print(p.val, '-> ', end='')
                p = p.next
            print(p.val)


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append_list([3, 4])
    l.print_list()
