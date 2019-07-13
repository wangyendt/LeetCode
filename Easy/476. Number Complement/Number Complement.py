# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 17:15
# software: PyCharm

class Solution:
    def findComplement(self, num: int) -> int:
        ret = ''
        for ni, n in enumerate(bin(num)):
            if ni > 1:
                ret += '1' if n == '0' else '0'
            else:
                ret += n
        return int(ret, 2)


so = Solution()
print(so.findComplement(5))
