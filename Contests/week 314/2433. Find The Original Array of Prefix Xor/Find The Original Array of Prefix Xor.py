"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find The Original Array of Prefix Xor.py
@time: 20221009
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ret = []
        for i, p in enumerate(pref):
            if not ret:
                ret.append(p)
                continue
            ret.append(pref[i - 1] ^ p)
        return ret


so = Solution()
print(so.findArray([5, 2, 0, 3, 1]))
