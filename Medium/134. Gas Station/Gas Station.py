# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 19:42
# software: PyCharm

class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        if sum(gas) < sum(cost):
            return -1
        l = 0
        r = (l + 1) % len(gas)
        remain = gas[0] - cost[0]
        while l != r:
            if remain >= 0:
                remain += gas[r] - cost[r]
                r = (r + 1) % len(gas)
            else:
                l = (l + len(gas) - 1) % len(gas)
                remain += gas[l] - cost[l]
        return l
