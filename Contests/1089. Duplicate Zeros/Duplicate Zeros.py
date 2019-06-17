# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/18 1:03
# software: PyCharm

class Solution:
    def duplicateZeros(self, arr: list) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return
        p = 0
        while p < len(arr):
            if arr[p] == 0:
                if p < len(arr) - 1:
                    q = len(arr) - 1
                    while q > p + 1:
                        arr[q] = arr[q - 1]
                        q -= 1
                    arr[p + 1] = 0
                    p += 1
            p += 1


so = Solution()
l = [1, 0, 2, 3, 0, 4, 5, 0]
l = [1, 2, 3]
so.duplicateZeros(l)
print(l)
