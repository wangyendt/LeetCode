#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Mice and Cheese.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        rew = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        res = sorted(range(len(rew)), key=lambda x: rew[x], reverse=True)
        ret = 0
        for i, r in enumerate(res):
            if i < k:
                ret += reward1[r]
            else:
                ret += reward2[r]
        return ret


so = Solution()
print(so.miceAndCheese(reward1=[1, 1], reward2=[1, 1], k=2))
