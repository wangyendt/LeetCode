#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Groups Entering a Competition.py 
@time: 2022/08/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import math
from typing import *


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)
