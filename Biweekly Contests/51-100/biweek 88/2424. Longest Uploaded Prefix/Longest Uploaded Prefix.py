#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Uploaded Prefix.py 
@time: 2022/10/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class LUPrefix:

    def __init__(self, n: int):
        self.cur = 0
        self.A = set()

    def upload(self, video: int) -> None:
        self.A.add(video)
        while self.cur + 1 in self.A:
            self.cur += 1

    def longest(self) -> int:
        return self.cur
