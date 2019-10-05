#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Balloons
@time: 2019/9/17 14:54
"""

import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = collections.Counter(text)
        return min(counter['b'],
                   counter['a'],
                   counter['l']//2,
                   counter['o']//2,
                   counter['n'])


so = Solution()
print(so.maxNumberOfBalloons(""))
print(so.maxNumberOfBalloons("nlaebolko"))
print(so.maxNumberOfBalloons("loonbalxballpoon"))
print(so.maxNumberOfBalloons("leetcode"))
