#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Maximum 69 Number
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/26 19:50
@Desc   ：
=================================================="""


class Solution:
    def maximum69Number(self, num: int) -> int:
        pos6 = str(num).find('6')
        if -1 == pos6:
            return num
        else:
            return int(str(num)[:pos6] + '9' + str(num)[pos6 + 1:])


so = Solution()
print(so.maximum69Number(966))
print(so.maximum69Number(9999))
