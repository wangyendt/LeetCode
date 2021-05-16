#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Incremental Memory Leak.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        cnt = 1
        while True:
            if memory1 < memory2:
                if memory2 < cnt:
                    break
                memory2 -= cnt
            else:
                if memory1 < cnt:
                    break
                memory1 -= cnt
            cnt += 1
        return [cnt, memory1, memory2]
