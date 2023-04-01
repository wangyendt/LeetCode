#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Making File Names Unique
@time: 2020/06/21 10:34
"""

import collections


class Solution:
    def getFolderNames(self, names: list) -> list:
        ret = []
        res = collections.defaultdict(int)
        for n in names:
            cur = n
            if n in res:
                k = res[n]
                while cur + '(' + str(k) + ')' in res:
                    k += 1
                cur = cur + '(' + str(k) + ')'
                res[cur] = 1
                res[n] = k
            else:
                res[n] = 1
            ret.append(cur)
        return ret


so = Solution()
print(so.getFolderNames(["pes", "fifa", "gta", "pes(2019)"]))
print(so.getFolderNames(["gta", "gta(1)", "gta", "avalon"]))
print(so.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
print(so.getFolderNames(["wano", "wano", "wano", "wano"]))
print(so.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]))
test = [f'res({k})' for k in range(100000)]
print(len(so.getFolderNames(test)))
