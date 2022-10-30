#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Stone Game VIII.py 
@time: 2021/05/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import itertools


class Solution:
    def stoneGameVIII(self, stones):
        ans = sum(stones)
        for num in list(itertools.accumulate(stones))[::-1][1:-1]:
            ans = max(ans, num - ans)
        return ans
