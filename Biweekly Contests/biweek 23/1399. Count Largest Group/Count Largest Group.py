#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Count Largest Group.py 
@time: 2020/04/08
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_of_digits_cnter = collections.Counter([sum(map(int, list(str(i)))) for i in range(1, n + 1)])
        max_len = sum_of_digits_cnter.most_common(1)[0][1]
        return sum([1 for k, v in sum_of_digits_cnter.items() if v == max_len], 0)


so = Solution()
print(so.countLargestGroup(13))
print(so.countLargestGroup(2))
print(so.countLargestGroup(15))
print(so.countLargestGroup(24))
