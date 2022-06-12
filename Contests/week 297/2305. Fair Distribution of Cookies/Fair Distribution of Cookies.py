#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Fair Distribution of Cookies.py 
@time: 2022/06/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import itertools
from typing import *


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ret = 1e10
        for p_c in itertools.permutations(cookies):
            for c_gap in itertools.combinations(range(len(cookies) - 1), k - 1):
                res = sum(p_c[c_gap[-1] + 1:])
                if res >= ret:
                    continue
                last = 0
                for cg in c_gap:
                    res = max(res, sum(p_c[last:cg + 1]))
                    last = cg + 1
                    if res >= ret:
                        break
                else:
                    ret = min(ret, res)
        return ret


so = Solution()
# print(so.distributeCookies(cookies=[8, 15, 10, 20, 8], k=2))
print(so.distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3))
