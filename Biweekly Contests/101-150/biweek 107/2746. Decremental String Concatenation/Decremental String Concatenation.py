"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Decremental String Concatenation.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import functools
from typing import *


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @functools.lru_cache(maxsize=None)
        def f(first, last, index):
            if len(words) - 1 < index:
                return 0
            w = words[index]
            return max((w[-1] == first) + f(w[0], last, index + 1), (last == w[0]) + f(first, w[-1], index + 1))

        return len(''.join(words)) - f(words[0][0], words[0][-1], 1)
