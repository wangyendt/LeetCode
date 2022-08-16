#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Merge Similar Items.py 
@time: 2022/08/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res1 = {i1: i2 for i1, i2 in items1}
        res2 = {i1: i2 for i1, i2 in items2}
        ret = {k: (res1[k] if k in res1 else 0) + (res2[k] if k in res2 else 0) for k in res1 | res2}
        return sorted([[kk, vv] for kk, vv in ret.items()])
