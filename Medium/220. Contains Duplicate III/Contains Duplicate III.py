# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/7 11:37
# software: PyCharm


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        d = dict()
        for i, n in enumerate(nums):
            bucket, offset = (n // t, 1) if t != 0 else (n, 0)
            for b in range(bucket - offset, bucket + offset + 1):
                if b in d and abs(i - d[b][0]) <= k and abs(n - d[b][1]) <= t:
                    return True
            d[bucket] = (i, n)
        return False


so = Solution()
print(so.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
