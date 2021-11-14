#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Time Needed to Buy Tickets.py 
@time: 2021/11/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ret = 0
        while tickets[k]:
            for i, t in enumerate(tickets):
                if t > 0:
                    tickets[i] = tickets[i] - 1
                    ret += 1
                if i == k:
                    if tickets[i] == 0:
                        return ret
