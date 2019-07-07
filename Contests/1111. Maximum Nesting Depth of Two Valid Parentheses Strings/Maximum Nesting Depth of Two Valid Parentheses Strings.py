#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Maximum Nesting Depth of Two Valid Parentheses Strings.py 
@time: 2019/07/07
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list:
        if not seq:
            return []
        maxDepth, p = 0, 0
        for s in seq:
            if s == '(':
                p += 1
                maxDepth = max(maxDepth, p)
        half = maxDepth // 2
        p = 0
        ret = [0] * len(seq)
        for si, s in enumerate(seq):
            if s == '(':
                p += 1
                if p > half:
                    ret[si] = 1
            else:
                if p > half:
                    ret[si] = 1
                p -= 1
        return ret
