#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Check If a String Contains All Binary Codes of Size K
@time: 2020/05/30 22:36
"""

import itertools


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for t in itertools.product('01', repeat=k):
            # print(''.join(t), s)
            if ''.join(t) not in s:
                return False
        return True


so = Solution()
print(so.hasAllCodes(s="00110110", k=2))
print(so.hasAllCodes(s="00110", k=2))
print(so.hasAllCodes(s="0110", k=1))
print(so.hasAllCodes(s="0110", k=2))
print(so.hasAllCodes(s="0000000001011100", k=4))
