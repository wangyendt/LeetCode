#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design an Ordered Stream.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0  # 0-indexed

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1  # 0-indexed
        self.data[id] = value
        if id > self.ptr: return []  # not reaching ptr

        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1

        return self.data[id:self.ptr]
