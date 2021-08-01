#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Weeks for Which You Can Work.py 
@time: 2021/08/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort(reverse=True)
        s = sum(milestones) - milestones[0]
        if s < milestones[0]:
            return min(s, milestones[0]) * 2 + 1
        return s + milestones[0]
