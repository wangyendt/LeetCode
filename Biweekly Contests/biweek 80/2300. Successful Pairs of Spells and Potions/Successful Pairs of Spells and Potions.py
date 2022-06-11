#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Successful Pairs of Spells and Potions.py 
@time: 2022/06/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import bisect
from typing import *


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ret = []
        for sp in spells:
            idx = bisect.bisect_left(potions, success / sp)
            # print(idx, sp)
            ret.append(len(potions) - idx)
        return ret


so = Solution()
print(so.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
