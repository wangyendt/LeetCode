"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count Pairs Of Similar Strings.py
@time: 20221218
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if set(words[i]) == set(words[j]):
                    ret += 1
        return ret
