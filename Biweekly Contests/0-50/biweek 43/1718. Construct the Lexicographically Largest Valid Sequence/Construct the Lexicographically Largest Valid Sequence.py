#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Construct the Lexicographically Largest Valid Sequence.py 
@time: 2021/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        mems = list(range(1, n + 1))
        mems.sort(reverse=True)
        place = list(range(2 * n - 1))
        ret = [0] * (2 * n - 1)

        def helper(ms, pl):
            if not ms:
                return True
            if not pl:
                return False
            next_pos = pl[0]
            if ret[next_pos] > 0:
                return helper(ms, pl[1:])
            for i, m in enumerate(ms):
                if m > 1 and next_pos + m < 2 * n - 1 and ret[next_pos + m] == 0:
                    ret[next_pos] = m
                    ret[next_pos + m] = m
                    if helper(ms[:i] + ms[i + 1:], pl[1:]):
                        return True
                    ret[next_pos] = 0
                    ret[next_pos + m] = 0
                else:
                    if m == 1:
                        ret[next_pos] = 1
                        if helper(ms[:i] + ms[i + 1:], pl[1:]):
                            return True
                        ret[next_pos] = 0
            return False

        helper(mems, place)
        return ret


so = Solution()
print(so.constructDistancedSequence(20))
