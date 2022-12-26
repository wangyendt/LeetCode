#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Shortest Distance to Target String in a Circular Array.py 
@time: 2022/12/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        n = len(words)
        indices = [i for i in range(n) if words[i] == target]
        return min(min(abs(startIndex - i), abs(n - abs(startIndex - i))) for i in indices)


so = Solution()
print(so.closetTarget(words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1))
