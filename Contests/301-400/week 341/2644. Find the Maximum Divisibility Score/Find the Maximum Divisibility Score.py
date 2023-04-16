"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Maximum Divisibility Score.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
from typing import *


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ret = 0
        score = collections.defaultdict(list)
        for d in divisors:
            res = 0
            for n in nums:
                if n % d == 0:
                    res += 1
            ret = max(ret, res)
            score[res].append(d)
        return min(score[ret])
