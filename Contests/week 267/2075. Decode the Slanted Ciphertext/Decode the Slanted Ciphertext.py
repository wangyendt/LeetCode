#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Decode the Slanted Ciphertext.py 
@time: 2021/11/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n_text = len(encodedText)
        res = [['' for _ in range(n_text // rows)] for _ in range(rows)]
        m, n = len(res), len(res[0])
        for i in range(m):
            for j in range(n):
                ptr = n * i + j
                res[i][j] = encodedText[ptr]
        ret = []
        ci, cj = 0, 0
        # [print(r) for r in res]
        while True:
            if ci >= m or cj >= n: break
            ret.append(res[ci][cj])
            if ci == m - 1:
                ci = 0
                cj = cj - (m - 1)
                cj += 1
            elif cj == n - 1:
                cj = cj - ci
                ci = 0
                cj += 1
            else:
                ci += 1
                cj += 1

        return ''.join(ret).rstrip(' ')


so = Solution()
# print(so.decodeCiphertext(encodedText="ch   ie   pr", rows=3))
print(so.decodeCiphertext(encodedText="iveo    eed   l te   olc", rows=4))
