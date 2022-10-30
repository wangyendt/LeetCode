#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Process Restricted Friend Requests.py 
@time: 2021/11/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys

sys.path.append('..')
from Tools.UnionFindSet import UnionFind
from copy import deepcopy


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        ret = []
        for i, r in enumerate(requests):
            r1, r2 = r
            tmp = UnionFind(n)
            tmp._id = uf._id[:]
            tmp._count = uf._count
            tmp._rank = uf._rank[:]
            tmp.union(r1, r2)
            # print(tmp)
            for restriction in restrictions:
                res1, res2 = restriction
                if tmp.connected(res1, res2):
                    ret.append(False)
                    break
            else:
                ret.append(True)
                uf.union(r1, r2)
                # uf = deepcopy(tmp)
        return ret


so = Solution()
print(so.friendRequests(n=5, restrictions=[[0, 1], [1, 2], [2, 3]], requests=[[0, 4], [1, 2], [3, 1], [3, 4]]))
