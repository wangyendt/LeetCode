"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Substring With Maximum Cost.py
@time: 20230401
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
from typing import *


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        set_chars = set(chars)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        val_dict = collections.defaultdict(int)
        for i, c in enumerate(chars):
            val_dict[c] = vals[i]
        for i, l in enumerate(letters):
            if l not in set_chars:
                val_dict[l] = i + 1
        max_cost = 0
        for i, t in enumerate(s):
            if t in val_dict:
                max_cost += val_dict[t]
            else:
                max_cost += vals[i]
        cur = 0
        max_cost = max(0, max_cost)
        # print(val_dict)
        for i, t in enumerate(s):
            cur += val_dict[t]
            if cur < 0:
                cur = 0
            max_cost = max(max_cost, cur)
        return max_cost


so = Solution()
print(so.maximumCostSubstring(s="adaa", chars="d", vals=[-1000]))
