#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Design Parking System
@time: 2020/10/03 22:30
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.A = dict()
        self.A[1] = big
        self.A[2] = medium
        self.A[3] = small

    def addCar(self, carType: int) -> bool:
        if self.A[carType] > 0:
            self.A[carType] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
