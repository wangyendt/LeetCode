#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: LRU Cache
@time: 2019/8/22 18:02
"""

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.size, self.cache = capacity, collections.OrderedDict()

    def get(self, key: int) -> int:
        val = self.cache.pop(key, None)
        if val is None: return -1
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if self.cache.pop(key, None) is None and self.size == len(self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value
