#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Reduce Array Size to The Half
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:21
@Desc   ：
=================================================="""

import collections


class Solution:
    def minSetSize(self, arr: list) -> int:
        res, n, ret = 0, len(arr), 0
        for k, v in collections.OrderedDict(
                sorted(collections.Counter(arr).items(), key=lambda x: x[1], reverse=True)).items():
            # print(f'k:{k},v:{v}')
            res += v
            ret += 1
            # print(res,n)
            if res >= n / 2:
                return ret


so = Solution()
print(so.minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(so.minSetSize(arr=[7, 7, 7, 7, 7, 7]))
print(so.minSetSize(arr=[1, 9]))
print(so.minSetSize(arr=[1000, 1000, 3, 7]))
print(so.minSetSize(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
