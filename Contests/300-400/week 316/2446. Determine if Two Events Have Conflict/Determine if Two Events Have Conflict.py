#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Determine if Two Events Have Conflict.py 
@time: 2022/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def get_minutes(event: str):
            return int(event[:2]) * 60 + int(event[-2:])

        e1 = list(map(get_minutes, event1))
        e2 = list(map(get_minutes, event2))
        if e1[1] < e2[0] or e2[1] < e1[0]: return False
        return True


so = Solution()
print(so.haveConflict(event1=["01:15", "02:00"], event2=["02:00", "03:00"]))
