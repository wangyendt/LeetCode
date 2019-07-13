# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 16:21
# software: PyCharm

class Solution:
    def findRadius(self, houses: list, heaters: list) -> int:
        if not heaters: return 0
        houses.sort()
        heaters.sort()
        if len(heaters) == 1: return max(heaters[0] - houses[0], houses[-1] - heaters[0])
        p, d = 0, 0
        for h in houses:
            while abs(h - heaters[p + 1]) <= abs(h - heaters[p]):
                cur = abs(h - heaters[p + 1])
                p += 1
                if p > len(heaters) - 2:
                    p = len(heaters) - 2
                    break
            else:
                cur = abs(h - heaters[p])
            d = max(d, cur)
        return d


so = Solution()
# print(so.findRadius([1, 2, 3], [2]))
# print(so.findRadius([1, 2, 3, 4], [1, 4]))
print(so.findRadius([1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499, 500, 501]))
