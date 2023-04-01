#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Kth Distinct String in an Array.py 
@time: 2021/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = 0
        cnter = collections.defaultdict(int)
        for a in arr:
            cnter[a] += 1
        for a in arr:
            if cnter[a] == 1:
                cnt += 1
                if cnt == k:
                    return a
        return ''
