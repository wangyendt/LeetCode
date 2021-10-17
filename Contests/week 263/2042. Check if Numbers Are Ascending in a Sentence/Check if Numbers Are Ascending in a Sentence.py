#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Numbers Are Ascending in a Sentence.py
@time: 2021/10/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        items = [int(t) for t in s.split(' ') if any(d in t for d in '1234567890')]
        return all(items[i] < items[i + 1] for i in range(len(items) - 1))


so = Solution()
print(so.areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(so.areNumbersAscending(s="hello world 5 x 5"))
