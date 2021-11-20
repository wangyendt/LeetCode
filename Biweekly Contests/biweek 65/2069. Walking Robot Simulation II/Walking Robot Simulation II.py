#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Walking Robot Simulation II.py 
@time: 2021/11/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Robot:

    def __init__(self, width: int, height: int):
        self.circle = (width + height - 2) * 2
        self.x = 0
        self.y = 0
        self.dir = 1
        self.cur = 0
        self.w, self.h = width, height

    def step(self, num: int) -> None:
        self.cur = (self.cur + num) % self.circle
        if 0 < self.cur <= self.w - 1:
            self.dir = 1
            self.x = self.cur
            self.y = 0
        elif self.w <= self.cur <= self.w + self.h - 2:
            self.dir = 2
            self.x = self.w - 1
            self.y = self.cur - self.w + 1
        elif self.w + self.h - 2 < self.cur <= self.w * 2 + self.h - 3:
            self.dir = 3
            self.x = self.w * 2 + self.h - 3 - self.cur
            self.y = self.h - 1
        else:
            self.dir = 4
            self.x = 0
            if self.cur == 0:
                self.y = 0
            else:
                self.y = self.circle - self.cur

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return {
            1: 'East',
            2: 'North',
            3: 'West',
            4: 'South'
        }[self.dir]
