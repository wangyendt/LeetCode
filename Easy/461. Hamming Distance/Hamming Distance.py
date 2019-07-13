# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 16:02
# software: PyCharm

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        while x or y:
            if x % 2 != y % 2:
                ret += 1
            x //= 2
            y //= 2
        return ret


so = Solution()
print(so.hammingDistance(1, 4))
