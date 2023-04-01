#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Check If N and Its Double Exist
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:24
@Desc   ：
=================================================="""


class Solution:
    def checkIfExist(self, arr: list) -> bool:
        if 0 in arr:
            arr.remove(0)
        arr = set(arr)

        for a in arr:
            if 2 * a in arr:
                return True
        return False


so = Solution()
print(so.checkIfExist(arr=[10, 2, 5, 3]))
print(so.checkIfExist(arr=[7, 1, 14, 11]))
print(so.checkIfExist(arr=[3, 1, 7, 11]))
