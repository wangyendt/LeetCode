#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Evaluate the Bracket Pairs of a String.py 
@time: 2021/03/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kns = collections.defaultdict(str)
        for kn in knowledge:
            kns[kn[0]] = kn[1]
        res = []
        b = False
        stack = []
        # print(kns)
        for ss in s:
            if not b:
                if ss == '(':
                    b = True
                else:
                    res.append(ss)
            else:
                if ss == ')':
                    t = ''.join(stack)
                    if t in kns:
                        res.extend(kns[t])
                    else:
                        res.append('?')
                    stack = []
                    b = False
                else:
                    stack.append(ss)
        return ''.join(res)


so = Solution()
print(so.evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
