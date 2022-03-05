#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sort the Jumbled Numbers.py 
@time: 2022/03/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        key_map = collections.defaultdict(int)

        def decode(num):
            s = str(num)
            ss = ''.join(map(lambda t: str(mapping[int(t)]), s))
            # print(ss)
            return int(ss, base=10)

        items = []
        for n in nums:
            items.append((n, decode(n)))
        # print(sorted(items, key=lambda x: x[1]))
        return list(k[0] for k in sorted(items, key=lambda x: x[1]))


so = Solution()
# print(so.sortJumbled(mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[789, 456, 123]))
# print(so.sortJumbled(mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]))
print(so.sortJumbled([8, 2, 9, 5, 3, 7, 1, 0, 6, 4],
                     [418, 4191, 916, 948, 629641556, 574, 111171937, 28250, 42775632, 6086, 85796326, 696292542, 186,
                      67559, 2167, 366, 854, 2441, 78176, 621, 4257, 2250097, 509847, 7506, 77, 50, 4135258, 4036,
                      59934, 59474, 3646243, 9049356, 85852, 90298188, 2448206, 30401413, 33190382, 968234660, 7973,
                      668786, 992777977, 77, 355766, 221, 246409664, 216290476, 45, 87, 836414, 40952]))
