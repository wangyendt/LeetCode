#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Binary Subsequence Less Than or Equal to K.py 
@time: 2022/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        left = []
        cnt = 0
        for i, t in enumerate(s):
            left.append(cnt)
            if t == '0':
                cnt += 1
        res = 0
        ret = 0
        print(left)
        for i, t in enumerate(s[::-1]):
            res += int(t) * 2 ** i
            if res <= k:
                ret = max(ret, left[~i] + i + 1)
        return ret


so = Solution()
print(so.longestSubsequence(s="00101001", k=1))
