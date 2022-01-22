#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Divide a Long Corridor.py 
@time: 2022/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt = 0
        odd_idx = []
        even_idx = []
        for i, c in enumerate(corridor):
            if c == 'S':
                cnt += 1
                if cnt % 2 == 0:
                    even_idx.append(i)
                else:
                    odd_idx.append(i)
        if cnt == 0: return 0
        if cnt & 1: return 0
        if cnt == 2: return 1
        ret = 1
        MOD = 10 ** 9 + 7
        even_idx = even_idx[:-1]
        odd_idx = odd_idx[1:]
        # odd_idx.append(len(corridor))
        for e, o in zip(even_idx, odd_idx):
            ret = (ret * (o - e)) % MOD
        return ret


so = Solution()
print(so.numberOfWays(corridor="SSPPSPS"))
print(so.numberOfWays("SSSPPPSPPSPSSSSSSPPPSPP"))
