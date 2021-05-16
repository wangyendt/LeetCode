#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Rotating the Box.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        def to_right():
            for i in range(m):
                des = n
                cnt = 0
                for j in range(n)[::-1]:
                    if box[i][j] == '*':
                        for k in range(j + 1, des - cnt):
                            box[i][k] = '.'
                        for k in range(des - cnt, des):
                            box[i][k] = '#'
                        des = j
                        cnt = 0
                    elif box[i][j] == '#':
                        cnt += 1
                for k in range(des - cnt):
                    box[i][k] = '.'
                for k in range(des - cnt, des):
                    box[i][k] = '#'

        def rotate():
            res = [['' for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    res[i][j] = box[m - 1 - j][i]
            return res

        to_right()
        # [print(b) for b in box]
        return rotate()


so = Solution()
print(so.rotateTheBox(box=[["#", ".", "#"]]))
print(so.rotateTheBox(box=[["#", ".", "*", "."],
                           ["#", "#", "*", "."]]))
print(so.rotateTheBox(box=[["#", "#", "*", ".", "*", "."],
                           ["#", "#", "#", "*", ".", "."],
                           ["#", "#", "#", ".", "#", "."]]))
