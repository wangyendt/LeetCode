#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Good Days to Rob the Bank.py 
@time: 2021/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return list(range(len(security)))
        if time * 2 + 1 > len(security): return []
        last = -1
        cnt1, cnt2 = collections.defaultdict(int), collections.defaultdict(int)
        for i, s in enumerate(security):
            if i > 0:
                if s <= last:
                    cnt1[i] = cnt1[i - 1] + 1
            last = s
        for i, s in enumerate(security[::-1]):
            if i > 0:
                if s <= last:
                    cnt2[len(security) - 1 - i] = cnt2[len(security) - 1 - i + 1] + 1
            last = s
        ret = []
        for i in range(len(security)):
            if cnt1[i] >= time and cnt2[i] >= time:
                ret.append(i)
        return ret
        # ret = set()
        # last = -1
        # stack = []
        # cnt = 0
        # cnt2 = 0
        # for i, s in enumerate(security):
        #     if s < last:
        #         cnt += 1
        #         if cnt >= time:
        #             stack.append(i)
        #         cnt2 = 0
        #     elif s == last:
        #         cnt += 1
        #         if cnt >= time:
        #             stack.append(i)
        #         cnt2 += 1
        #         while stack:
        #             diff = i - stack[0]
        #             if diff == time:
        #                 if cnt2 >= time and time <= i <= len(security) - 1 - time:
        #                     ret.add(stack.pop(0))
        #                 else:
        #                     break
        #             else:
        #                 break
        #     else:
        #         print(i, s, stack, cnt, cnt2)
        #         while stack:
        #             diff = i - stack[0]
        #             if diff == time:
        #                 tmp = stack.pop(0)
        #                 if cnt2 >= time and time <= i <= len(security) - 1 - time:
        #                     ret.add(tmp)
        #             elif diff < time:
        #                 break
        #             else:
        #                 stack.pop(0)
        #     last = s
        # return list(ret)


so = Solution()
print(so.goodDaysToRobBank(security=[5, 3, 3, 3, 5, 6, 2], time=2))
print(so.goodDaysToRobBank(security=[5, 3, 3, 3, 5, 4, 3, 2, 1, 2, 3, 6, 2], time=1))
print(so.goodDaysToRobBank(security=[5, 3, 3, 3, 5, 6, 6, 6, 6, 6, 2], time=2))
print(so.goodDaysToRobBank(security=[2, 2, 2, 2], time=2))
print(so.goodDaysToRobBank(security=[2, 2, 2, 2, 2], time=2))
print(so.goodDaysToRobBank(security=[2, 2, 2, 2, 2, 2], time=2))
print(so.goodDaysToRobBank([0, 4, 3, 0, 0, 0], 1))
