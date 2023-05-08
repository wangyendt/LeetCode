"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Number of Adjacent Elements With the Same Color.py
@time: 20230508
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0] * n
        ret = []
        c = 0
        for i, q in queries:
            left, right = arr[i - 1] if i > 0 else 0, arr[i + 1] if i < n - 1 else 0
            if arr[i] and arr[i] == left: c -= 1
            if arr[i] and arr[i] == right: c -= 1
            arr[i] = q
            if arr[i] == left: c += 1
            if arr[i] == right: c += 1
            ret.append(c)
        return ret
