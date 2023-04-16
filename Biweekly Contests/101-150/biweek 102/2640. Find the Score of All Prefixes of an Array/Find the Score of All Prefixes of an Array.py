"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Score of All Prefixes of an Array.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ret = []
        mx = 0
        for i, n in enumerate(nums):
            mx = max(mx, n)
            ret.append(mx + n)
        ans = [0]
        for r in ret:
            ans.append(ans[-1] + r)
        return ans[1:]
