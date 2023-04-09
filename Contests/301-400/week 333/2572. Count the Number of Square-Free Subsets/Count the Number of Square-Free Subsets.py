"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count the Number of Square-Free Subsets.py
@time: 20230331
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        candidates = set([2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30])
        cnt = collections.defaultdict(int)
        for num in nums:
            if num in candidates:
                cnt[num] += 1

        def count(arr):
            if not arr:
                return 1
            arr1 = []
            for num in arr[1:]:
                if math.gcd(num, arr[0]) == 1:
                    arr1.append(num)
            return (count(arr[1:]) + cnt[arr[0]] * count(arr1)) % MOD

        ones = nums.count(1)
        tmp = 1
        for _ in range(ones):
            tmp = (tmp * 2) % MOD
        return (count(list(cnt)) * tmp - 1) % MOD
