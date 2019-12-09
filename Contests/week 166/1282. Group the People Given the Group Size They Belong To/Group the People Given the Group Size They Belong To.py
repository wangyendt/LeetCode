#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Group the People Given the Group Size They Belong To
@time: 2019/12/9 15:34
"""

import collections


class Solution:
    def groupThePeople(self, groupSizes: list) -> list(list()):
        kv_dict = collections.defaultdict(list)
        for gi, gs in enumerate(groupSizes):
            kv_dict[gs].append(gi)
        ret = []
        for k, v in kv_dict.items():
            for i in range(len(v) // k):
                ret.append(v[i * k:(i + 1) * k])
        return ret


so = Solution()
print(so.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
print(so.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
