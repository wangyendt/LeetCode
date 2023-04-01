#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Check If String Is Transformable With Substring Sort Operations
@time: 2020/09/13 12:21
"""

import collections


# Very tricky question!
#
# Probably the hardest part is to realize that: For every digit in t you find the first occurrence in s. Call that current digit as key. We need to make sure in s, no digit smaller than key appears to the left.
# As we check one-by-one, we need to remove the digits we considered from s. In order to do this operation constant time, store all indices in reversed form using stack. Then use the pop operation in the second loop.
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # places: this stores the indices of every digit from 0 to 9
        places = collections.defaultdict(list)
        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)

        for e in t:  # we loop over t and check every digit
            key = int(e)  # key: our current digit
            if not places[key]:
                return False  # digit is not in s, return False
            i = places[key][-1]  # i: location of our current digit
            for j in range(key):  # only loop over digits smaller then current digit
                if places[j]:
                    if places[j][-1] < i:  # there is a digit smaller then current digit, return false
                        return False
            places[key].pop()

        return True
