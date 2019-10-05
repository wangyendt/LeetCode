# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/15 23:47
# software: PyCharm


class Solution:
    def permute(self, S: str) -> list:
        S = S.replace('{', '.').replace('}', '.').strip('.')
        backup = S.split('.')
        backup = [b.split(',') if len(b.split(',')) > 1 else [b] for b in backup]
        allRet = []

        def helper(arr, res):
            if not arr:
                allRet.append(res)
            else:
                stack = arr[0]
                for si, s in enumerate(stack):
                    helper(arr[1:], res + s)

        helper(backup, '')
        return sorted(allRet)


so = Solution()
# print(so.permute('{a,b}c{d,e}f'))
print(so.permute("{a,b}{z,x,y}"))
