#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Execution of All Suffix Instructions Staying in a Grid.py 
@time: 2021/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        dr = {
            'U': -1, 'D': 1, 'L': 0, 'R': 0
        }
        dc = {
            'U': 0, 'D': 0, 'L': -1, 'R': 1
        }
        ret = []
        for i in range(m):
            spr, spc = startPos
            for j in range(i, m):
                print(i, j, spr, spc,s[j])
                spr += dr[s[j]]
                spc += dc[s[j]]
                if spr < 0 or spr >= n or spc < 0 or spc >= n:
                    ret.append(j - i)
                    break
            else:
                ret.append(m - i)
        return ret


so = Solution()
print(so.executeInstructions(n=3, startPos=[0, 1], s="RRDDLU"))
