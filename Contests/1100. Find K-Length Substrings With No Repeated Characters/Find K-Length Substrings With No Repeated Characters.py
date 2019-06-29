#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:  wangye
@file: Find K-Length Substrings With No Repeated Characters.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K > 26:
            return 0
        else:
            ret = 0
            for i in range(len(S) - K + 1):
                if len(set(S[i:i + K])) == K:
                    print(S[i:i + K])
                    ret += 1
            return ret


so = Solution()
print(so.numKLenSubstrNoRepeats("havefunonleetcode", 5))
