# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 19:30
# software: PyCharm


class Solution:
    def checkRecord(self, s: str) -> bool:
        cntA, cntLL = 0, 0
        for si, su in enumerate(s):
            if su == 'A':
                cntA += 1
            if s[si:si + 3] == 'LLL':
                return False
            if cntA > 1:
                return False
        return True


so = Solution()
print(so.checkRecord('PPALLP'), True)
print(so.checkRecord('PPALLL'), False)
