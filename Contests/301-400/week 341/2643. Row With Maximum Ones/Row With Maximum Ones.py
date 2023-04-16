"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Row With Maximum Ones.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import collections
import itertools
from typing import *


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = collections.defaultdict(int)
        for i, j in itertools.product(range(len(mat)), range(len(mat[0]))):
            if mat[i][j] == 1:
                res[i] += 1
        mx_ones = 0
        ret = [0, 0]
        for i in range(len(mat)):
            if mx_ones < res[i]:
                mx_ones = res[i]
                ret = [i, res[i]]
        return ret


so = Solution()
print(so.rowAndMaximumOnes(mat=[[0, 1], [1, 0]]))
