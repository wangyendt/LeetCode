# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/15 23:59
# software: PyCharm

class Solution:
    def confusingNumberII(self, N: int) -> int:
        tranDic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        jumpDic = {'2': '6', '3': '6', '4': '6', '5': '6', '7': '8'}

        def trans(ss):
            for si in range(len(ss) // 2 + 1):
                if tranDic[ss[si]] != ss[-1 - si]:
                    return True
            return False

        ret = 0
        i, last = 4, 4
        while i <= N:
            x = i
            if any([uv in str(x) for uv in '23457']):
                strx = str(x)
                for sxi, sx in enumerate(strx):
                    if sx in '23457':
                        x = int(strx[:sxi] + jumpDic[sx] + strx[sxi + 1:])
            else:
                if trans(str(x)):
                    ret += 1
                x += 1
            i, last = x, i
        return ret


so = Solution()

import time

start = time.time()
# for i in range(6, 4000000):
#     so.confusingNumberII(i)
# print(so.confusingNumberII(20))
# print(so.confusingNumberII(100))
# print(so.confusingNumberII(999928))
# print(so.confusingNumberII(3999819))
print(so.confusingNumberII(1000000000))
print(time.time() - start)
