#!/usr/bin/python
# coding: utf-8
# @Time    : 2022/2/6 2:28
# @Author  : Ye Wang (Wayne)
# @Email   : wang121ye@hotmail.com
# @File    : Minimum Cost to Set Cooking Time.py
# @Software: PyCharm


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        d, r = divmod(targetSeconds, 60)
        t1 = ''
        if d < 100:
            t1 = (str(d) if d > 0 else '') + ('00' if r == 0 else ((('0' if d > 0 else '') if r < 10 else '') + str(r)))
        t2 = ''
        if r <= 39 and d > 0:
            t2 = (str(d - 1) if d > 1 else '') + str(r + 60)
        ret = int(1e10)

        # print(f'{t1=},{t2=}')

        def make(target: str):
            res = 0
            sa = startAt
            for i, t in enumerate(target):
                if sa != int(t):
                    res += moveCost
                res += pushCost
                # print(f'{i=},{t=},{sa=},{res=}')
                sa = int(t)
            return res

        if t1:
            ret = min(ret, make(t1))
        if t2:
            ret = min(ret, make(t2))
        return ret


so = Solution()
print(so.minCostSetTime(startAt=1, moveCost=2, pushCost=1, targetSeconds=600))
print(so.minCostSetTime(0, 1, 4, 9))
print(so.minCostSetTime(0, 100000, 100000, 6039))
print(so.minCostSetTime(0, 1, 2, 76))
