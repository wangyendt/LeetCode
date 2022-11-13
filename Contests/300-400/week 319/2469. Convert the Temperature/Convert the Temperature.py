#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Convert the Temperature.py 
@time: 2022/11/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, 1.8 * celsius + 32]
