#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Binary String After Change
@time: 2020/12/27 00:27
"""


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        binary = list(binary)
        n = len(binary)
        res = ''
        zeros = [i for i, k in enumerate(binary) if k == '0']
        for i in range(n):
            if binary[i] == '1':
                res += '1'
                continue
            else:
                zeros.pop(0)
                if i < n - 1:
                    if binary[i + 1] == '0':
                        res += '1'
                    else:
                        if not zeros:
                            res += '0'
                            continue
                        else:
                            next_0_idx = zeros[0]
                            binary[next_0_idx] = '1'
                            binary[i + 1] = '0'
                            zeros[0] = i + 1
                            res += '1'
                else:
                    res += '0'
        return res
