#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Seat Reservation Manager.py 
@time: 2021/05/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import heapq


class SeatManager:

    def __init__(self, n: int):
        self.h = []
        for i in range(n):
            heapq.heappush(self.h, i + 1)

    def reserve(self) -> int:
        return heapq.heappop(self.h)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
