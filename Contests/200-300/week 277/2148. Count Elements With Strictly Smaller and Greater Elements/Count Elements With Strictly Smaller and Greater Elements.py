#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Elements With Strictly Smaller and Greater Elements.py 
@time: 2022/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countElements(self, nums: List[int]) -> int:
        m, M = min(nums), max(nums)
        return len([n for n in nums if n not in (m, M)])
