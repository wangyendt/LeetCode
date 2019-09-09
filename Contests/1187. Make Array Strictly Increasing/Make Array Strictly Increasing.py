# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/8 12:43
# software: PyCharm

import bisect
import collections
import functools


class Solution:
    def makeArrayIncreasing1(self, arr1: list, arr2: list) -> int:
        l = sorted(set(arr2))

        @functools.lru_cache(None)
        def min_changes(i, cur_min):
            if i >= len(arr1):
                return 0

            j = bisect.bisect_right(l, cur_min)
            swap_cost = 1 + min_changes(i + 1, l[j]) if j < len(l) else float("+inf")
            keep_cost = min_changes(i + 1, arr1[i]) if arr1[i] > cur_min else float("+inf")

            return min(swap_cost, keep_cost)

        changes = min_changes(0, float("-inf"))
        return changes if changes != float("+inf") else -1

    def makeArrayIncreasing2(self, arr1: list, arr2: list) -> int:
        dp = {-1: 0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                print(i, key, dp.items())
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1


so = Solution()
print(so.makeArrayIncreasing1([1, 5, 3, 6, 7], [1, 3, 2, 4]))
