"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find Maximum Number of String Pairs.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set(words)
        ret = 0
        for w in words:
            if w in word_set and w[::-1] in word_set and w != w[::-1]:
                ret += 1
                word_set.remove(w)
                if w[::-1] in word_set:
                    word_set.remove(w[::-1])
        return ret
