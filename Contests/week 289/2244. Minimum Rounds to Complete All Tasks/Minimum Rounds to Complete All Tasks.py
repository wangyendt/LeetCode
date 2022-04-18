#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Rounds to Complete All Tasks.py 
@time: 2022/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = collections.Counter(tasks)
        keys = sorted(res.keys())
        ret = 0
        for k in keys:
            m, r = divmod(res[k], 3)
            if r == 1:
                if res[k] > 1:
                    ret += m + 1
                else:
                    return -1
            else:
                ret += m if r == 0 else m + 1
        return ret


so = Solution()
print(so.minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(so.minimumRounds(tasks=[5, 5, 5, 5]))
print(so.minimumRounds(tasks=[5]))
