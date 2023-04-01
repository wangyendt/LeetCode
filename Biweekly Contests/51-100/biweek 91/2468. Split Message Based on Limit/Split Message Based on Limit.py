#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Split Message Based on Limit.py 
@time: 2022/11/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        l, r = 0, len(message)

        def is_possible(n):
            rem = len(message)
            for i in range(1, n + 1):
                used = 3 + len(str(i)) + len(str(n))
                taken = limit - used
                rem -= taken

            return rem <= 0

        while l < r:
            mid = (l + r) // 2

            if is_possible(mid):
                r = mid
            else:
                l = mid + 1

        if not is_possible(l):
            return []

        ret = []

        mptr = 0

        for i in range(1, l + 1):
            used = 3 + len(str(i)) + len(str(l))

            curr = message[mptr:mptr + (limit - used)]
            mptr += (limit - used)

            ret.append(curr + "<{0}/{1}>".format(str(i), str(l)))

        return ret
