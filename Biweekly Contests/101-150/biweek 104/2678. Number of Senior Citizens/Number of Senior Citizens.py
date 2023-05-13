#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Senior Citizens.py 
@time: 2023/05/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 for d in details if int(d[-4:-2]) > 60])
