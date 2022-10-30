#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find All People With Secret.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import itertools


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        can = {0, firstPerson}
        for _, grp in itertools.groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            stack = set()
            graph = collections.defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                if x in can: stack.add(x)
                if y in can: stack.add(y)

            stack = list(stack)
            while stack:
                x = stack.pop()
                for y in graph[x]:
                    if y not in can:
                        can.add(y)
                        stack.append(y)
        return can
