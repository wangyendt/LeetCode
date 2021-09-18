#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Original Array From Doubled Array.py 
@time: 2021/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ret = []
        while changed:
            p = changed.pop()
            idx = bisect.bisect_right(changed, p // 2)
            if idx == 0: return []
            # print(f'{changed=},{idx=},{changed[idx-1]=},{p=}')
            if changed[idx - 1] * 2 == p:
                changed[idx - 1:idx] = []
                ret.append(p // 2)
            else:
                return []
        return ret


so = Solution()
print(so.findOriginalArray([1, 3, 4, 2, 6, 8]))
print(so.findOriginalArray([1, 3, 7, 5, 2, 6, 14, 10]))
print(so.findOriginalArray([1, 3, 7, 15, 2, 6, 14, 20]))
