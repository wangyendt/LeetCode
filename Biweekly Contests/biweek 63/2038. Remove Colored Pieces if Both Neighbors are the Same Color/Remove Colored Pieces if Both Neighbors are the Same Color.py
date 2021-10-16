#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Remove Colored Pieces if Both Neighbors are the Same Color.py 
@time: 2021/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        s = {
            'A': 0,
            'B': 0
        }
        last = 'C'
        cnt = 1
        for c in colors:
            if c == last:
                cnt += 1
                if cnt >= 3:
                    s[c] += 1
            else:
                cnt = 1
            last = c
        return s['A'] > s['B']


so = Solution()
print(so.winnerOfGame(colors="AAABABB"))
print(so.winnerOfGame(colors="BB"))
print(so.winnerOfGame(colors="AA"))
print(so.winnerOfGame(colors="AAA"))
print(so.winnerOfGame(colors="AAAA"))
print(so.winnerOfGame(colors=""))
print(so.winnerOfGame(colors="B"))
