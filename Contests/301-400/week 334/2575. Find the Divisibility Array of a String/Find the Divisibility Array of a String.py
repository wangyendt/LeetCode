"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Divisibility Array of a String.py
@time: 20230627
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        cur = 0
        ret = []
        for i, w in enumerate(word):
            cur += int(w)
            if cur % m == 0:
                ret.append(1)
            else:
                ret.append(0)
            cur = cur * 10
            cur = cur % m
        return ret
