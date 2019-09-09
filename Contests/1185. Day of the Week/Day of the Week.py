# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/8 11:30
# software: PyCharm


import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        today = datetime.datetime.strptime(' '.join((str(year), str(month), str(day))), '%Y %m %d')
        return week[today.weekday()]


so = Solution()
print(so.dayOfTheWeek(6, 9, 2019))
