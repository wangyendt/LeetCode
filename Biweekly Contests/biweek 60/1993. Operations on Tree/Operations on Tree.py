#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Operations on Tree.py 
@time: 2021/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys

sys.path.append('../..')
from Tools import API_utils
from Tools.API_utils import call_me
import collections


class LockingTree:

    def __init__(self, parent: List[int]):
        self.par = collections.defaultdict(int)
        self.ch = collections.defaultdict(set)
        self.locker = collections.defaultdict(int)
        for i, p in enumerate(parent):
            self.par[i] = p
            self.ch[p].add(i)
            self.locker[i] = -1

    def lock(self, num: int, user: int) -> bool:
        if self.locker[num] == -1:
            self.locker[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locker[num] == user:
            self.locker[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def find_ch(i, this):
            if this.locker[i] != -1:
                return True
            for c in this.ch[i]:
                if find_ch(c, this):
                    break
            else:
                return False
            return True

        def unlock_(node, this):
            for c in this.ch[node]:
                this.locker[c] = -1
                unlock_(c, this)

        if self.locker[num] == -1:
            if find_ch(num, self):
                cur_ = cur = num
                while cur in self.par:
                    if self.locker[cur] != -1:
                        break
                    cur = self.par[cur]
                else:
                    self.locker[num] = user
                    unlock_(num, self)
                    return True
                return False


call_me(LockingTree, ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"],
        [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]])
call_me(LockingTree,
        ["LockingTree", "upgrade", "upgrade", "upgrade", "upgrade", "unlock", "unlock", "upgrade", "upgrade", "upgrade","lock", "lock", "upgrade", "upgrade", "unlock", "upgrade", "upgrade", "upgrade", "upgrade", "unlock",         "unlock"],
        [[[-1, 6, 5, 5, 7, 0, 7, 0, 0, 6]], [5, 3], [2, 3], [7, 39], [1, 32], [5, 44], [2, 15], [1, 11], [1, 18],[3, 7], [5, 36], [5, 42], [8, 5], [1, 19], [3, 38], [0, 27], [4, 11], [9, 2], [8, 41], [5, 36], [7, 29]])
