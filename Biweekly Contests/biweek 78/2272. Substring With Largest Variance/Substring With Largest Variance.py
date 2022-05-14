#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Substring With Largest Variance.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def largestVariance(self, s: str) -> int:
        last = collections.defaultdict(int)
        cnt = collections.defaultdict(int)
        ret = 0
        pos = [[0 for _ in range(26)] for _ in range(26)]
        min_mat = [[0 for _ in range(26)] for _ in range(26)]
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i, cur in enumerate(s):
            last[cur] = i
            cnt[cur] += 1
            now = ord(cur) - ord('a')
            for j, z in enumerate(letters):
                if cur != z and cnt[z] > 0:
                    res = ret
                    ret = max(cnt[cur] - cnt[z] - min_mat[now][j] - (last[letters[j]] == pos[now][j]),
                              cnt[z] - cnt[cur] - min_mat[j][now] - (last[letters[j]] == pos[j][now]))
                    ret = max(ret, res)
            for j, z in enumerate(letters):
                if cnt[cur] - cnt[z] < min_mat[now][j]:
                    min_mat[now][j] = cnt[cur] - cnt[z]
                    pos[now][j] = i
                if cnt[z] - cnt[cur] < min_mat[j][now]:
                    min_mat[j][now] = cnt[z] - cnt[cur]
                    pos[j][now] = i
        return ret


so = Solution()
print(so.largestVariance(s="aababbb"))
