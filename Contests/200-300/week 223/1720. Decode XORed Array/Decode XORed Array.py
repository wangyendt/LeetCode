#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Decode XORed Array.py 
@time: 2021/01/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for en in encoded:
            ret.append(ret[-1] ^ en)
        return ret
