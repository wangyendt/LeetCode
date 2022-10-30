#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Divide a String Into Groups of Size k.py 
@time: 2022/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        if l % k != 0:
            m, d = divmod(l, k)
            s = s + fill * (k - d)
        return [s[i:i + k] for i in range(0, len(s) - k + 1, k)]
