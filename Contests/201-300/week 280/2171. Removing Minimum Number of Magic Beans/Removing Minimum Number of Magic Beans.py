#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Removing Minimum Number of Magic Beans.py 
@time: 2022/02/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        sb = sum(beans)
        ret = sb
        l = len(beans)
        for i in range(1, max(beans) + 1):
            idx = bisect.bisect_left(beans, i)
            ret = min(ret, sb - (l - idx) * i)
            # print(beans, i, ret, idx)
        return ret


so = Solution()
print(so.minimumRemoval([4, 1, 6, 5]))
