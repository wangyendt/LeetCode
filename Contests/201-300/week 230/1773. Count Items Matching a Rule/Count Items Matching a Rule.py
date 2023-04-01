#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Items Matching a Rule.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = {
            'type': collections.defaultdict(int),
            'color': collections.defaultdict(int),
            'name': collections.defaultdict(int),
        }
        for t, c, n in items:
            res['type'][t] += 1
            res['color'][c] += 1
            res['name'][n] += 1
        return res[ruleKey][ruleValue]
