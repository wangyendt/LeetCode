# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/15 23:34
# software: PyCharm
class Solution:
    def highFive(self, items: list(list())) -> list(list()):
        dic = {}
        for it in items:
            if dic.get(it[0]):
                dic[it[0]].append(it[1])
            else:
                dic[it[0]] = [it[1]]

        ret = []
        for d in dic.keys():
            tmp = sorted(dic[d])
            ret.append([d, sum(tmp[-5:]) // (min(5, len(tmp[-5:])))])
        return ret


so = Solution()
print(
    so.highFive([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
