#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Naming a Company.py 
@time: 2022/06/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count = collections.defaultdict(set)
        for a in ideas:
            count[a[0]].add(hash(a[1:]))
        res = 0
        for a, seta in count.items():
            for b, setb in count.items():
                if a >= b: continue
                same = len(seta & setb)
                res += (len(seta) - same) * (len(setb) - same)
        return res * 2
