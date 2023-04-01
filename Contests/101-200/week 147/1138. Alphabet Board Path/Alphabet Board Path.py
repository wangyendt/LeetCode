#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Alphabet Board Path.py 
@time: 2019/07/28
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        coord = collections.defaultdict(tuple)
        for i, l in enumerate('abcdefghijklmnopqrstuvwxyz'):
            coord[l] = (i // 5, i % 5)
        stack = ['a']
        ret = ''
        for tar in target:
            s = stack.pop()
            if tar != s:
                tar_y, tar_x = coord[tar]
                s_y, s_x = coord[s]
                if tar_x < s_x:
                    ret += 'L' * (s_x - tar_x)
                if tar_y < s_y:
                    ret += 'U' * (s_y - tar_y)
                if tar_x > s_x:
                    ret += 'R' * (tar_x - s_x)
                if tar_y > s_y:
                    ret += 'D' * (tar_y - s_y)
            ret += '!'
            stack.append(tar)
        return ret


so = Solution()
print(so.alphabetBoardPath('leet'))
print(so.alphabetBoardPath('code'))
