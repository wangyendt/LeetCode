# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/19 14:30
# software: PyCharm
from collections import defaultdict


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == '':
            return s2 == s3
        if s2 == '':
            return s1 == s3
        if len(s3) != len(s1) + len(s2):
            return False
        n = len(s3)
        # dic restore the num of s1 of possible combination of s1 and s2
        dic = defaultdict(set)
        for i in range(1, n + 1):
            if i == 1:
                if s1[i - 1] == s3[i - 1]:
                    dic[i].add(1)
                if s2[i - 1] == s3[i - 1]:
                    dic[i].add(0)
            else:
                for j in dic[i - 1]:
                    if j < len(s1) and s3[i - 1] == s1[j]:
                        dic[i].add(j + 1)
                    if i - 1 - j < len(s2) and s3[i - 1] == s2[i - 1 - j]:
                        dic[i].add(j)
                if not dic[i]:
                    return False
        return not dic[n] is None


so = Solution()
print(so.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
print(so.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
print(so.isInterleave('', '', 'aadbbcbcac'))
