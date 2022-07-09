#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: The Latest Time to Catch a Bus.py 
@time: 2022/07/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import bisect
from typing import *


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passengers = [p for p in passengers if p <= buses[-1]]
        last = 0
        p_set = set(passengers)
        ret = 0
        for i, b in enumerate(buses):
            idx = bisect.bisect_right(passengers, b, lo=last)
            if last >= len(passengers):
                ret = max(ret, b)
                continue
            if last + capacity > len(passengers):
                ret = max(ret, buses[-1])
            elif last + capacity == len(passengers):
                ret = max(ret, passengers[-1] - 1)
            else:
                ret = max(ret, passengers[last + capacity - 1] - 1)
            last = min(last + capacity, idx)
        while ret in p_set:
            ret -= 1
        return min(ret, buses[-1])


so = Solution()
print(so.latestTimeCatchTheBus(buses=[10, 20], passengers=[2, 17, 18, 19], capacity=2))
print(so.latestTimeCatchTheBus(buses=[20, 30, 10], passengers=[19, 13, 26, 4, 25, 11, 21], capacity=2))
print(so.latestTimeCatchTheBus([2], [2], 2))
print(so.latestTimeCatchTheBus([5], [7, 8], 1))
print(so.latestTimeCatchTheBus([10, 20], [2, 15], 3))
print(so.latestTimeCatchTheBus([3], [2, 4], 2))
print(so.latestTimeCatchTheBus([6, 8, 18, 17], [6, 8, 17], 1))
print(so.latestTimeCatchTheBus(
    [2241, 1239, 4280, 5025, 4354, 1749, 6310, 7993, 8163, 9369, 342, 6387, 9147, 8985, 3055, 1406, 42, 8060, 1583,
     5844, 5553, 119, 8043, 7836, 4159, 5512, 9230, 1220, 1893, 9411, 8319, 862, 6689, 7209, 1305, 8958, 6658, 8909,
     9351, 9070, 9586, 7175, 9251, 7514, 2850, 6390, 6355, 1551, 8513, 843, 8170, 4831, 6342, 8849, 2879, 8937, 2755,
     5890, 7293, 1737, 4324, 2034, 7425, 9785, 1354, 6476, 3059, 6526, 8193, 9537, 2749, 8541, 5187, 8219, 369, 8467,
     8140, 8175, 7287, 2598, 415, 2306, 1781, 1555, 3388, 622, 7574, 4537, 4833, 1023, 4841, 7482, 6518, 4941, 9758,
     7583, 1341, 5981, 6687, 6450],
    [8218, 5861, 7144, 1315, 9370, 846, 7541, 6688, 6348, 3526, 1343, 8043, 6326, 8697, 1738, 8306, 7292, 9506, 8537,
     2827, 15, 3310, 1848, 1668, 8487, 9785, 3059, 7480, 5403, 8165, 6474, 2384, 8913, 1914, 9555, 6197, 4912, 502, 646,
     5837, 5940, 1366, 3012, 5074, 4254, 5545, 4841, 6520, 9138, 2877, 1252, 2755, 9039, 9359, 4832, 7185, 8889, 2653,
     7576, 1512, 7863, 9712, 2102, 1239, 329, 1750, 4787, 2280, 5012, 7486, 6662, 411, 6368, 8098, 6481, 1557, 8161,
     8449, 1553, 9349, 9232, 4284, 24560, 72, 7276, 8045, 906, 8942, 7405, 7710, 8176, 8172, 6388, 1135, 6638, 4325,
     356, 9216, 8959, 4507, 6406],
    5))
