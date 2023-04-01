#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Cells in a Range on an Excel Sheet.py 
@time: 2022/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        s_ch, s_num = start
        e_ch, e_num = end
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = {k: i for i, k in enumerate(letters)}
        ret = []
        for i in range(res[s_ch], res[e_ch] + 1):
            for j in range(int(s_num), int(e_num) + 1):
                ret.append(letters[i] + str(j))
        return ret


so = Solution()
print(so.cellsInRange(s="K1:L2"))
