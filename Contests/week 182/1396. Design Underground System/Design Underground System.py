#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Design Underground System.py 
@time: 2020/04/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import sys

sys.path.append('..')
from Tools.API_utils import *


class UndergroundSystem:

    def __init__(self):
        self.A = dict()
        self.B = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.A:
            self.A[stationName] = dict()
        self.A[stationName][id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.B:
            self.B[stationName] = dict()
        self.B[stationName][id] = t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ret, n = 0, 0
        for k, v in self.A[startStation].items():
            if k in self.B[endStation]:
                ret += self.B[endStation][k] - self.A[startStation][k]
                n += 1
        return ret / n


callers = ["UndergroundSystem", "checkIn", "checkIn", "checkIn", "checkOut", "checkOut", "checkOut", "getAverageTime",
           "getAverageTime", "checkIn", "getAverageTime", "checkOut", "getAverageTime"]

params = [[], [45, "Leyton", 3], [32, "Paradise", 8], [27, "Leyton", 10], [45, "Waterloo", 15], [27, "Waterloo", 20],
          [32, "Cambridge", 22], ["Paradise", "Cambridge"], ["Leyton", "Waterloo"], [10, "Leyton", 24],
          ["Leyton", "Waterloo"],
          [10, "Waterloo", 38], ["Leyton", "Waterloo"]]

call_me(UndergroundSystem, callers, params)
