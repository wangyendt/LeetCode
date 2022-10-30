#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of People to Teach.py 
@time: 2021/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import collections
from copy import deepcopy


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        seen2 = collections.defaultdict(set)
        for i, l in enumerate(languages):
            for ll in l:
                seen2[i + 1].add(ll)
        ret = 1000
        for i in range(1, n + 1):
            cnt = 0
            res = 0
            adds = []
            for f1, f2 in friendships:
                if seen2[f1] & seen2[f2]:
                    cnt += 1
                else:
                    if i not in seen2[f1] and i not in seen2[f2]:
                        res += 2
                        seen2[f1].add(i)
                        seen2[f2].add(i)
                        adds.append((f1, i))
                        adds.append((f2, i))
                    else:
                        res += 1
                        if i in seen2[f1]:
                            seen2[f2].add(i)
                            adds.append((f2, i))
                        else:
                            seen2[f1].add(i)
                            adds.append((f1, i))
                if res >= ret:
                    continue
            if cnt == len(friendships):
                return 0
            for a1, a2 in adds:
                seen2[a1].remove(a2)
            ret = min(ret, res)
        return ret


so = Solution()
print(so.minimumTeachings(n=3, languages=[[2], [1, 3], [1, 2], [3]], friendships=[[1, 4], [1, 2], [3, 4], [2, 3]]))
