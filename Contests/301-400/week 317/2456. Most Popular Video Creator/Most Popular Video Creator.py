#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Most Popular Video Creator.py 
@time: 2022/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cnter = collections.defaultdict(int)
        for i, c in enumerate(creators):
            cnter[c] += views[i]
        mx = sorted(cnter.items(), key=lambda x: (-x[1]))[0][1]
        # print(cnter, mx)
        res = collections.defaultdict(list)
        for c, i, v in zip(creators, ids, views):
            if cnter[c] == mx:
                res[c].append([v, i])
        ret = []
        for k, vl in res.items():
            # print(k, vl)
            sub_max = sorted(vl, key=lambda x: (-x[0], x[1]))
            ret.append([k, sub_max[0][1]])
        return ret
