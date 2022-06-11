#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Match Substring After Replacement.py 
@time: 2022/06/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        h = collections.defaultdict(set)
        for a, b in mappings:
            h[a].add(b)
        l = len(sub)
        for i in range(len(s) - len(sub) + 1):
            flag = True
            for s_val, sub_val in zip(s[i:i + l], sub):
                if s_val == sub_val or (s_val in h[sub_val]):
                    continue
                else:
                    flag = False
                    break
            if flag:
                return True
        return False


so = Solution()
print(so.matchReplacement(s="fool3e7bar", sub="leet", mappings=[["e", "3"], ["t", "7"], ["t", "8"]]))
print(so.matchReplacement(s="fooleetbar", sub="f00l", mappings=[["o", "0"]]))
print(so.matchReplacement(s="Fool33tbaR", sub="leetd",
                          mappings=[["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]]))
print(so.matchReplacement("gfnk9rmyi1a4zvxzvt1ze0g",
                          "gfnk9rmyi1a4zvxzv71zeo",
                          [["4", "a"], ["1", "l"], ["o", "0"], ["l", "i"], ["e", "3"], ["7", "t"]]))
print(so.matchReplacement(
    "llllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrlllllllllllllllllllllllllllllllll",
    "lllllllllllllllllllllllllllllllll",
    [["l", "a"], ["l", "b"], ["l", "c"], ["l", "d"], ["l", "e"], ["l", "f"], ["l", "g"], ["l", "h"], ["l", "i"],
     ["l", "j"], ["l", "k"], ["l", "m"], ["l", "n"], ["l", "o"], ["l", "p"], ["l", "q"], ["l", "s"], ["l", "t"],
     ["l", "u"], ["l", "v"], ["l", "w"], ["l", "x"], ["l", "y"], ["l", "z"], ["l", "0"], ["l", "1"], ["l", "2"],
     ["l", "3"], ["l", "4"], ["l", "5"], ["l", "6"], ["l", "7"], ["l", "8"], ["l", "9"], ["r", "a"], ["r", "b"],
     ["r", "c"], ["r", "d"], ["r", "e"], ["r", "f"], ["r", "g"], ["r", "h"], ["r", "i"], ["r", "j"], ["r", "k"],
     ["r", "m"], ["r", "n"], ["r", "o"], ["r", "p"], ["r", "q"], ["r", "s"], ["r", "t"], ["r", "u"], ["r", "v"],
     ["r", "w"], ["r", "x"], ["r", "y"], ["r", "z"], ["r", "0"], ["r", "1"], ["r", "2"], ["r", "3"], ["r", "4"],
     ["r", "5"], ["r", "6"], ["r", "7"], ["r", "8"], ["r", "9"]]))
