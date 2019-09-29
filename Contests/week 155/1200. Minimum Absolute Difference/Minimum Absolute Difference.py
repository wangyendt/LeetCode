# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 16:58
# software: PyCharm


class Solution:
    def minimumAbsDifference(self, arr: list) -> list(list()):
        arr.sort()
        abs_diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        min_abs_diff = min(abs_diff)
        res = [i for i, a in enumerate(abs_diff) if a == min_abs_diff]
        ret = [[arr[i], arr[i + 1]] for i in res]
        return ret


so = Solution()
print(so.minimumAbsDifference([4, 2, 1, 3]))
print(so.minimumAbsDifference([1, 3, 6, 10, 15]))
print(so.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
print(so.minimumAbsDifference(list(range(100000))))
