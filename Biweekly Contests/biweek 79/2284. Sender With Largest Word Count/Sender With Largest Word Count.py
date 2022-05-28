#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sender With Largest Word Count.py 
@time: 2022/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        res = collections.defaultdict(int)
        for i, (s, m) in enumerate(zip(senders, messages)):
            res[s] += len(m.split(' '))
        # print(res)
        return sorted(res.items(), key=lambda x: (x[1], x[0]))[-1][0]


so = Solution()
print(so.largestWordCount(messages=["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"],
                          senders=["Alice", "userTwo", "userThree", "Alice"]))
