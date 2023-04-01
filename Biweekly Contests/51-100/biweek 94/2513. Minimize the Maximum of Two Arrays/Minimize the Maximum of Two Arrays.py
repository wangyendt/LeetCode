#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize the Maximum of Two Arrays.py 
@time: 2022/12/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import math
from math import gcd, lcm


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low, high = 1, 10 ** 20
        while low < high:
            mid = (low + high) >> 1
            x = mid - mid // divisor1
            y = mid - mid // divisor2
            both = mid - mid // lcm(divisor1, divisor2)
            # print(mid, x, y, both, x >= uniqueCnt1 and y >= uniqueCnt2 and both >= uniqueCnt1+uniqueCnt2)
            if x >= uniqueCnt1 and y >= uniqueCnt2 and both >= uniqueCnt1 + uniqueCnt2:
                high = mid
            else:
                low = mid + 1
        # print('#')
        return low


so = Solution()
print(so.minimizeSet(divisor1=2, divisor2=7, uniqueCnt1=1, uniqueCnt2=3))
print(so.minimizeSet(divisor1=3, divisor2=5, uniqueCnt1=2, uniqueCnt2=1))
print(so.minimizeSet(divisor1=2, divisor2=4, uniqueCnt1=8, uniqueCnt2=2))
