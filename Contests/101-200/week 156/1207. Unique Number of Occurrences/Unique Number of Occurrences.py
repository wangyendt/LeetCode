# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 11:31
# software: PyCharm


import collections


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        return len(arr) == sum(set([v for k, v in collections.Counter(arr).items()]))

so = Solution()
print(so.uniqueOccurrences([1,2,2,1,1,3]))
print(so.uniqueOccurrences([1,2]))
print(so.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))