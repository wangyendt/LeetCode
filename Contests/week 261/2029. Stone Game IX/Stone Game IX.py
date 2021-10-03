# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Stone Game IX.py
@time: 2021/10/04
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        A = stones
        A = [a % 3 for a in A]
        cnter = collections.Counter(A)
        res1 = False
        s = 0
        # print(cnter)
        for i, a in enumerate(A):
            carry = 0
            if i & 1:
                if cnter[0] > 0:
                    cnter[0] -= 1
                    carry = 0
                else:
                    if s % 3 == 1:
                        if cnter[1] == 0:
                            res1 = True
                            break
                        else:
                            cnter[1] -= 1
                            carry = 1
                    elif s % 3 == 2:
                        if cnter[2] == 0:
                            res1 = True
                            break
                        else:
                            cnter[2] -= 1
                            carry = 2
                    else:
                        print('error')
            elif i == 0:
                if cnter[1] == 0:
                    if cnter[2] == 0: return False
                    res1 = False
                    break
                else:
                    cnter[1] -= 1
                    carry = 1
            else:
                if cnter[0] > 0:
                    cnter[0] -= 1
                    carry = 0
                else:
                    if s % 3 == 1:
                        if cnter[1] == 0:
                            res1 = False
                            break
                        else:
                            cnter[1] -= 1
                            carry = 1
                    elif s % 3 == 2:
                        if cnter[2] == 0:
                            res1 = False
                            break
                        else:
                            cnter[2] -= 1
                            carry = 2
                    else:
                        print('error')
            s = (s + carry) % 3

        cnter = collections.Counter(A)
        res2 = False
        s = 0
        for i, a in enumerate(A):
            carry = 0
            if i & 1:
                if cnter[0] > 0:
                    cnter[0] -= 1
                    carry = 0
                else:
                    if s % 3 == 1:
                        if cnter[1] == 0:
                            res2 = True
                            break
                        else:
                            cnter[1] -= 1
                            carry = 1
                    elif s % 3 == 2:
                        if cnter[2] == 0:
                            res2 = True
                            break
                        else:
                            cnter[2] -= 1
                            carry = 2
                    else:
                        print('error')
            elif i == 0:
                if cnter[2] == 0:
                    if cnter[1] == 0: return False
                    res2 = False
                    break
                else:
                    cnter[2] -= 1
                    carry = 2
            else:
                if cnter[0] > 0:
                    cnter[0] -= 1
                    carry = 0
                else:
                    if s % 3 == 1:
                        if cnter[1] == 0:
                            res2 = False
                            break
                        else:
                            cnter[1] -= 1
                            carry = 1
                    else:
                        if cnter[2] == 0:
                            res2 = False
                            break
                        else:
                            cnter[2] -= 1
                            carry = 2
            s = (s + carry) % 3

        return res1 or res2


so = Solution()
print(so.stoneGameIX([20, 3, 20, 17, 2, 12, 15, 17, 4]))
