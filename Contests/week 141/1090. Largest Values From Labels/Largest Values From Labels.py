# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/24 10:30
# software: PyCharm

from collections import Counter


class Solution:
    def largestValsFromLabels(self, values: list, labels: list, num_wanted: int, use_limit: int) -> int:
        cnt1, cnt2 = Counter(labels), Counter(labels)
        arr = sorted(zip(values, labels), key=lambda x: x[0])[::-1]
        ret, cnt = 0, 0
        for a in arr:
            if cnt2[a[1]] - cnt1[a[1]] < use_limit:
                ret += a[0]
                cnt1[a[1]] -= 1
                cnt += 1
                if cnt == num_wanted:
                    break
        return ret


so = Solution()
print(so.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], num_wanted=3, use_limit=1))
print(so.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], num_wanted=3, use_limit=2))
print(so.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=1))
print(so.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=2))
