"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Extra Characters in a String.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import functools
from typing import *


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        N = len(s)

        @functools.lru_cache(None)
        def helper(t: str) -> int:
            if not t: return 0
            ret = N
            for tt in dictionary:
                if t[:len(tt)] == tt:
                    ret = min(ret, helper(t[len(tt):]))
            ret = min(ret, 1 + helper(t[1:]))
            return ret

        return helper(s)


so = Solution()
print(so.minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))
print(so.minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]))
print(so.minExtraChar(s="metzeaencgpgvsckjrqafkxgyzbe", dictionary=["zdzz", "lgrhy", "r", "ohk", "zkowk", "g", "zqpn", "anoni", "ka", "qafkx", "t", "jr", "xdye", "mppc", "bqqb", "encgp", "yf", "vl", "ctsxk", "gn", "cujh", "ce", "rwrpq", "tze", "zxhg", "yzbe", "c", "o", "hnk", "gv", "uzbc", "xn", "kk", "ujjd", "vv", "mxhmv", "ugn", "at", "kumr", "ensv", "x", "uy", "gb", "ae", "jljuo", "xqkgj"]))
