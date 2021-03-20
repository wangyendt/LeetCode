#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design Authentication Manager.py 
@time: 2021/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.k = timeToLive
        self.A = collections.defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.A[tokenId] = currentTime + self.k

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.A:
            if currentTime < self.A[tokenId]:
                self.A[tokenId] = currentTime + self.k
            else:
                self.A.pop(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = []
        cnt = 0
        for k, v in self.A.items():
            if currentTime < v:
                cnt += 1
            else:
                res.append(k)
        for r in res:
            self.A.pop(r)
        return cnt

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
