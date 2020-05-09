#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/10 1:46
@Author:  wang121ye
@File: Find the Kth Smallest Sum of a Matrix With Sorted Rows.py
@Software: PyCharm
"""


class Solution:
    def helper(self, mat, k):
        result = [n for n in mat[0]] if len(mat) == 1 else [s + n for s in self.helper(mat[1:], k) for n in mat[0]]
        # if k is large, dont sort since it will get sorted later
        return sorted(result)[:k] if len(result) > k else result

    def kthSmallest(self, mat: list(list()), k: int) -> int:
        return self.helper(mat, k)[k - 1]
