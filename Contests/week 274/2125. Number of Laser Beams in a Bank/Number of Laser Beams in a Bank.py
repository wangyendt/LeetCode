#!/usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: 2125. Number of Laser Beams in a Bank.py 
@time: 2022/01/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = 0
        ret = 0
        for b in bank:
            res = sum(1 for t in b if t == '1')
            if res > 0:
                ret += last * res
                last = res
        return ret
