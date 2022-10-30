#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Angle Between Hands of a Clock
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/22 3:25
@Desc   ：
=================================================="""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_minute = 360 * minutes / 60
        angle_hour = 360 * hour / 12 + 30 * minutes / 60
        return min([
            abs(angle_minute - angle_hour), 360 - (abs(angle_minute - angle_hour))
        ])


so = Solution()
print(so.angleClock(12, 30), 165)
print(so.angleClock(3, 30), 75)
print(so.angleClock(3, 15), 7.5)
print(so.angleClock(4, 50), 155)
print(so.angleClock(12, 0), 0)
