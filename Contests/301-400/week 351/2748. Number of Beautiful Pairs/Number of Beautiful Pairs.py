"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Number of Beautiful Pairs.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import math
import operator
from typing import *


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        N = len(nums)
        ret = 0

        def get_first_digit(num):
            while num >= 10:
                num //= 10
            return num

        first_digits = list(map(get_first_digit, nums))
        last_digits = list(map(lambda x: x % 10, nums))
        for i in range(N):
            for j in range(i + 1, N):
                if math.gcd(first_digits[i], last_digits[j]) == 1:
                    ret += 1
        return ret


so = Solution()
print(so.countBeautifulPairs([31, 25, 72, 79, 74]))
