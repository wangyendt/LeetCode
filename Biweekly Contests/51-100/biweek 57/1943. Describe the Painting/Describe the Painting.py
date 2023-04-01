#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Describe the Painting.py 
@time: 2021/07/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        res = collections.defaultdict(int)
        for s, e, c in segments:
            res[s] += c
            res[e] -= c
        # print(res)
        ret = []
        pre, c = None, 0
        for r in sorted(res):
            # print(r)
            if pre and c != 0:
                ret.append([pre, r, c])
            c += res[r]
            pre = r
        return ret


so = Solution()
print(so.splitPainting(segments=[[1, 4, 5], [4, 7, 7], [1, 7, 9]]))
