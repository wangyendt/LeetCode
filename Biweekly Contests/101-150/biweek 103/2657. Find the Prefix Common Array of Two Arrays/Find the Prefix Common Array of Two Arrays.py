"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Prefix Common Array of Two Arrays.py
@time: 20230505
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa, sb = set(), set()
        ret = []
        for i, (a, b) in enumerate(zip(A, B)):
            sa.add(a)
            sb.add(b)
            ret.append(len(sa & sb))
        return ret
