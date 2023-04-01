#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Make Array Zero by Subtracting Equal Amounts.py 
@time: 2022/08/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([n for n in nums if n]))
