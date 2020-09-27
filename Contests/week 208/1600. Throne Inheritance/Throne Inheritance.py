# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Throne Inheritance.py
@time: 2020/09/27
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Tree:
    def __init__(self, me, lvl=0):
        self.me = me
        self.child = []
        self.lvl = lvl

    def find(self, name):
        if self.me == name:
            return self, self.lvl
        else:
            for ch in self.child:
                res = ch.find(name)
                if res: return res
            return None, -1

    def append(self, father, son):
        tr, idx = self.find(father)
        if tr:
            ret = Tree(son, idx + 1)
            tr.child.append(ret)
            return ret

    def traverse(self):
        ret = [self.me]
        if not self.child:
            return ret
        else:
            for ch in self.child:
                ret += ch.traverse()
            return ret


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inh_ord = Tree(kingName)
        self.dead = set()
        self.search_dict = {kingName: self.inh_ord}

    def birth(self, parentName: str, childName: str) -> None:
        tr = self.search_dict[parentName]
        res = tr.append(parentName, childName)
        self.search_dict[childName] = res

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return [ch for ch in self.inh_ord.traverse() if ch not in self.dead]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance('king')
# obj.birth('king', 'andy')
# obj.birth('king', 'bob')
# obj.birth('king', 'catherine')
# obj.birth('andy', 'matthew')
# obj.birth('bob', 'alex')
# obj.birth('bob', 'asha')
# param_3 = obj.getInheritanceOrder()
# print(param_3)
# obj.death('bob')
# param_3 = obj.getInheritanceOrder()
# print(param_3)

null = 'null'
A = ["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
B = [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"],
     [null]]
obj = None
for a, b in zip(A, B):
    res = null
    if a == 'ThroneInheritance':
        obj = ThroneInheritance('king')
    elif a == 'birth':
        obj.birth(b[0], b[1])
    elif a == 'death':
        obj.death(b[0])
    elif a == 'getInheritanceOrder':
        res = obj.getInheritanceOrder()
        print(res)
